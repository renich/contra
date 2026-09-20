#!/usr/bin/env python3
"""
scripts/contra-cli.py - Command-line interface for Contra Model Context Protocol (MCP)
Allows quick querying of profile, services, portfolio, messages, and job feed.
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error

TOKEN_PATH = os.path.expanduser("~/.gemini/antigravity-cli/mcp_oauth_tokens.json")
MCP_CONFIG_PATH = os.path.expanduser("~/.gemini/config/mcp_config.json")
MCP_URL = "https://contra.com/mcp"
TOKEN_ENDPOINT = "https://contra.com/api/mcp/oauth/token"

def get_token():
    if not os.path.exists(TOKEN_PATH):
        sys.stderr.write(f"Error: Token file not found at {TOKEN_PATH}\nRun scripts/auth-contra.bash first.\n")
        sys.exit(1)
    with open(TOKEN_PATH) as f:
        data = json.load(f)
    token = data.get("contra", {}).get("access_token")
    if not token:
        sys.stderr.write("Error: 'access_token' missing in token file.\n")
        sys.exit(1)
    return token

def refresh_oauth_token():
    if not os.path.exists(TOKEN_PATH):
        return None
    with open(TOKEN_PATH) as f:
        data = json.load(f)
    c = data.get("contra", {})
    client_id = c.get("client_id")
    refresh_token = c.get("refresh_token")
    if not client_id or not refresh_token:
        return None

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id
    }
    req = urllib.request.Request(
        TOKEN_ENDPOINT,
        data=urllib.parse.urlencode(payload).encode("utf-8"),
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            new_access = res.get("access_token")
            new_refresh = res.get("refresh_token", refresh_token)
            c["access_token"] = new_access
            c["refresh_token"] = new_refresh
            data["contra"] = c
            with open(TOKEN_PATH, "w") as f:
                json.dump(data, f, indent=2)
            if os.path.exists(MCP_CONFIG_PATH):
                try:
                    with open(MCP_CONFIG_PATH) as cf:
                        cfg = json.load(cf)
                    if "mcpServers" in cfg and "contra" in cfg["mcpServers"]:
                        cfg["mcpServers"]["contra"]["headers"]["Authorization"] = f"Bearer {new_access}"
                        with open(MCP_CONFIG_PATH, "w") as cf:
                            json.dump(cfg, cf, indent=2)
                except Exception:
                    pass
            return new_access
    except Exception as e:
        sys.stderr.write(f"Token refresh failed: {e}\n")
        return None

def call_tool(tool_name, arguments=None, retried=False):
    token = get_token()
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments or {}
        }
    }
    req = urllib.request.Request(
        MCP_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "Authorization": f"Bearer {token}"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            text = resp.read().decode("utf-8")
            for line in text.splitlines():
                if line.startswith("data: "):
                    return json.loads(line[6:])
    except urllib.error.HTTPError as e:
        if e.code == 401 and not retried:
            sys.stderr.write("401 Unauthorized received. Automatically refreshing OAuth token...\n")
            if refresh_oauth_token():
                return call_tool(tool_name, arguments, retried=True)
        sys.stderr.write(f"HTTP Error {e.code}: {e.reason}\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Request failed: {e}\n")
        sys.exit(1)
    return None

def cmd_status(args):
    who = call_tool("whoami")
    sc = who.get("result", {}).get("structuredContent", {})
    visitor = sc.get("visitor", {}).get("userAccount", {})
    profile = visitor.get("profile", {})
    print("=== Contra MCP Authentication & Identity ===")
    print(f"Name:        {profile.get('firstName')} {profile.get('lastName')}")
    print(f"Username:    {profile.get('displayUsername')}")
    print(f"Email:       {visitor.get('emailAddress')}")
    print(f"Profile URL: https://contra.com/{profile.get('displayUsername')}")

    intake = call_tool("get_co_agent_intake_settings")
    isc = intake.get("result", {}).get("structuredContent", {})
    enabled = isc.get("isIntakeAgentEnabled")
    print(f"Co-Agent:    {'ENABLED' if enabled else 'DISABLED'}")

def cmd_services(args):
    who = call_tool("whoami")
    username = who.get("result", {}).get("structuredContent", {}).get("visitor", {}).get("userAccount", {}).get("profile", {}).get("displayUsername")
    res = call_tool("list_services", {"username": username})
    services = res.get("result", {}).get("structuredContent", {}).get("services", [])
    print(f"=== Published Services ({len(services)}) ===")
    for s in services:
        title = s.get("title")
        p = s.get("price", {})
        ptype = p.get("type")
        amount = p.get("amount")
        interval = p.get("interval")
        price_str = f"${amount} ({ptype})" if not interval else f"${amount}/{interval.lower()} ({ptype})"
        url = s.get("serviceUrl")
        print(f"* {title}")
        print(f"  Pricing: {price_str}")
        print(f"  URL:     {url}")

def cmd_projects(args):
    who = call_tool("whoami")
    username = who.get("result", {}).get("structuredContent", {}).get("visitor", {}).get("userAccount", {}).get("profile", {}).get("displayUsername")
    res = call_tool("list_portfolio_projects", {"username": username, "includeDrafts": True})
    sc = res.get("result", {}).get("structuredContent", {})
    projects = sc.get("projects", [])
    print(f"=== Portfolio Projects ({sc.get('totalCount', len(projects))}) ===")
    for p in projects:
        title = p.get("title")
        slug = p.get("slug")
        roles = ", ".join(p.get("roles", []))
        is_draft = p.get("isDraft", False)
        status = "[DRAFT]" if is_draft else "[PUBLISHED]"
        print(f"* {status} {title}")
        print(f"  Roles: {roles}")
        print(f"  URL:   https://contra.com/p/{slug}")

def cmd_messages(args):
    res = call_tool("list_chat_conversations")
    sc = res.get("result", {}).get("structuredContent", {})
    convs = sc.get("conversations", [])
    print(f"=== Active Conversations ({len(convs)}) ===")
    if not convs:
        print("No active chat conversations.")
    for c in convs:
        cid = c.get("id")
        title = c.get("title")
        unread = c.get("unreadCount", 0)
        print(f"* {title} (ID: {cid}) - {unread} unread messages")

def cmd_feed(args):
    res = call_tool("list_job_feed", {"preset": "ALL", "first": args.limit})
    sc = res.get("result", {}).get("structuredContent", {})
    entries = sc.get("entries", [])
    print(f"=== Contra Job Feed ({len(entries)} items shown, total: {sc.get('totalCount')}) ===")
    for e in entries:
        j = e.get("job", {})
        title = j.get("title")
        roles = ", ".join(j.get("roles", []))
        b = j.get("budget", {})
        btype = b.get("type", "")
        fmin = b.get("feeMin", "")
        fmax = b.get("feeMax", "")
        url = j.get("publicUrl")
        print(f"* {title} | {btype} {fmin}-{fmax}")
        print(f"  Roles: {roles}")
        print(f"  URL:   {url}")

def cmd_raw(args):
    payload = json.loads(args.json_args) if args.json_args else {}
    res = call_tool(args.tool_name, payload)
    print(json.dumps(res, indent=2))

def main():
    parser = argparse.ArgumentParser(description="Contra MCP CLI Helper")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="Show current account identity and intake agent status")
    sub.add_parser("services", help="List published productized services")
    sub.add_parser("projects", help="List portfolio projects and drafts")
    sub.add_parser("messages", help="List chat conversations and unread status")
    
    p_feed = sub.add_parser("feed", help="Browse open jobs on Contra")
    p_feed.add_argument("--limit", type=int, default=10, help="Max entries to return")

    p_raw = sub.add_parser("raw", help="Call any Contra MCP tool directly")
    p_raw.add_argument("tool_name", help="Name of the MCP tool")
    p_raw.add_argument("json_args", nargs="?", default="{}", help="JSON arguments string")

    args = parser.parse_args()
    cmds = {
        "status": cmd_status,
        "services": cmd_services,
        "projects": cmd_projects,
        "messages": cmd_messages,
        "feed": cmd_feed,
        "raw": cmd_raw
    }
    cmds[args.command](args)

if __name__ == "__main__":
    main()
