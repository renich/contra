#!/usr/bin/env python3
"""
scripts/auth-contra.py - Interactive OAuth 2.0 PKCE authenticator for Contra MCP
Registers dynamic client, opens authorization window, exchanges code, and saves Bearer token.
"""

import os
import sys
import json
import base64
import hashlib
import urllib.request
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess

PORT = 8765
REDIRECT_URI = f"http://127.0.0.1:{PORT}/callback"
REGISTRATION_ENDPOINT = "https://contra.com/api/mcp/oauth/register"
AUTHORIZATION_ENDPOINT = "https://contra.com/api/mcp/oauth/authorize"
TOKEN_ENDPOINT = "https://contra.com/api/mcp/oauth/token"
MCP_CONFIG_PATH = os.path.expanduser("~/.gemini/config/mcp_config.json")
MCP_OAUTH_TOKENS_PATH = os.path.expanduser("~/.gemini/antigravity-cli/mcp_oauth_tokens.json")

auth_code = None

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/callback":
            params = urllib.parse.parse_qs(parsed.query)
            if "code" in params:
                auth_code = params["code"][0]
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                html = """
                <!DOCTYPE html>
                <html>
                <head><title>Contra MCP Authorized</title></head>
                <body style="font-family: system-ui, -apple-system, sans-serif; background: #111; color: #eee; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 90vh;">
                  <div style="background: #1e1e2e; border: 1px solid #a6e3a1; padding: 40px; border-radius: 12px; text-align: center; max-width: 500px;">
                    <h1 style="color: #a6e3a1; margin-top: 0;">✓ Contra MCP Authorized</h1>
                    <p style="color: #cdd6f4; font-size: 16px;">Antigravity has received your authorization token.</p>
                    <p style="color: #a6adc8; font-size: 14px;">You can close this tab and return to your terminal.</p>
                  </div>
                </body>
                </html>
                """
                self.wfile.write(html.encode("utf-8"))
            elif "error" in params:
                error = params.get("error_description", params["error"])[0]
                self.send_response(400)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(f"<h2>Authorization Failed</h2><p>{error}</p>".encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass

def generate_pkce():
    code_verifier = base64.urlsafe_b64encode(os.urandom(32)).decode("utf-8").rstrip("=")
    code_challenge = base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode("utf-8")).digest()).decode("utf-8").rstrip("=")
    return code_verifier, code_challenge

def register_client():
    print("1. Registering dynamic OAuth client with Contra...")
    req_data = {
        "client_name": "Antigravity",
        "redirect_uris": [REDIRECT_URI]
    }
    req = urllib.request.Request(
        REGISTRATION_ENDPOINT,
        data=json.dumps(req_data).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "Antigravity/1.0"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        client_id = res["client_id"]
        print(f"   Registered successfully! Client ID: {client_id}")
        return client_id

def exchange_code(client_id, code, code_verifier):
    print("3. Exchanging authorization code for Bearer tokens...")
    token_payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": client_id,
        "code_verifier": code_verifier
    }
    req = urllib.request.Request(
        TOKEN_ENDPOINT,
        data=json.dumps(token_payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "Antigravity/1.0"}
    )
    with urllib.request.urlopen(req) as resp:
        tokens = json.loads(resp.read().decode("utf-8"))
        return tokens

def update_configs(tokens, client_id):
    access_token = tokens["access_token"]
    refresh_token = tokens.get("refresh_token")
    
    # 1. Update ~/.gemini/config/mcp_config.json
    print(f"4. Updating {MCP_CONFIG_PATH} with Authorization header...")
    mcp_config = {}
    if os.path.exists(MCP_CONFIG_PATH):
        try:
            with open(MCP_CONFIG_PATH, "r") as f:
                mcp_config = json.load(f)
        except Exception:
            mcp_config = {}
    
    if "mcpServers" not in mcp_config:
        mcp_config["mcpServers"] = {}
        
    mcp_config["mcpServers"]["contra"] = {
        "disabled": False,
        "serverUrl": "https://contra.com/mcp",
        "headers": {
            "Authorization": f"Bearer {access_token}"
        }
    }
    
    with open(MCP_CONFIG_PATH, "w") as f:
        json.dump(mcp_config, f, indent=2)
    print("   mcp_config.json updated!")

    # 2. Update ~/.gemini/antigravity-cli/mcp_oauth_tokens.json
    oauth_tokens = {}
    if os.path.exists(MCP_OAUTH_TOKENS_PATH):
        try:
            with open(MCP_OAUTH_TOKENS_PATH, "r") as f:
                oauth_tokens = json.load(f)
        except Exception:
            oauth_tokens = {}
            
    oauth_tokens["contra"] = {
        "client_id": client_id,
        "access_token": access_token,
        "refresh_token": refresh_token,
        "endpoint": "https://contra.com/mcp"
    }
    
    with open(MCP_OAUTH_TOKENS_PATH, "w") as f:
        json.dump(oauth_tokens, f, indent=2)
    print(f"   Saved token bundle to {MCP_OAUTH_TOKENS_PATH}!")

def main():
    code_verifier, code_challenge = generate_pkce()
    client_id = register_client()
    
    auth_params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": "mcp:tools",
        "code_challenge": code_challenge,
        "code_challenge_method": "S256"
    }
    auth_url = f"{AUTHORIZATION_ENDPOINT}?{urllib.parse.urlencode(auth_params)}"
    
    server = HTTPServer(("127.0.0.1", PORT), OAuthCallbackHandler)
    server.timeout = 120
    
    print("\n" + "=" * 60)
    print("Please authorize Contra MCP in your browser:")
    print(f"\n{auth_url}\n")
    print("=" * 60 + "\n")
    
    # Attempt to open browser automatically
    try:
        subprocess.run(["xdg-open", auth_url], check=False)
    except Exception:
        pass
        
    print("Waiting for browser authorization callback on http://127.0.0.1:8765/callback ...")
    while auth_code is None:
        server.handle_request()
        
    if not auth_code:
        print("Error: No authorization code received.")
        sys.exit(1)
        
    tokens = exchange_code(client_id, auth_code, code_verifier)
    update_configs(tokens, client_id)
    
    print("\n✓ Authentication successful! Contra MCP is fully configured.")

if __name__ == "__main__":
    main()
