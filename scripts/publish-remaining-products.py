#!/usr/bin/env python3
"""
scripts/publish-remaining-products.py
Publishes Product 2 and Product 3 with cover images, and updates Services with covers.
"""

import os
import sys
import json
import urllib.request
import urllib.error

TOKEN_PATH = os.path.expanduser("~/.gemini/antigravity-cli/mcp_oauth_tokens.json")
MCP_URL = "https://contra.com/mcp"

def get_token():
    with open(TOKEN_PATH) as f:
        data = json.load(f)
    return data["contra"]["access_token"]

def call_tool(tool_name, arguments):
    token = get_token()
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
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
    with urllib.request.urlopen(req) as resp:
        text = resp.read().decode("utf-8")
        for line in text.splitlines():
            if line.startswith("data: "):
                res = json.loads(line[6:])
                if "error" in res:
                    raise RuntimeError(f"Tool error: {res['error']}")
                struct = res.get("result", {}).get("structuredContent")
                if struct:
                    return struct
                content_text = res.get("result", {}).get("content", [{}])[0].get("text", "")
                if content_text:
                    return json.loads(content_text)
                return res.get("result")
    raise RuntimeError("No response data received")

def publish_product(data):
    print(f"\n--- Preparing Digital Product: {data['title']} ---")
    prep = call_tool("create_product_prepare", data)
    draft_id = prep.get("draftId")
    if not draft_id:
        raise RuntimeError(f"Failed to prepare product: {prep}")
    print(f"Prepared! Draft ID: {draft_id}")
    print(f"--- Confirming Digital Product: {data['title']} ---")
    conf = call_tool("create_product_confirm", {"confirm": True, "draftId": draft_id})
    prod = conf.get("product", {})
    print(f"✓ Confirmed & Published! Slug: {prod.get('slug')}")
    print(f"  URL: {prod.get('productUrl')}")
    return conf

def update_service_cover(slug, cover_url):
    print(f"\n--- Adding Cover to Service: {slug} ---")
    prep = call_tool("update_productized_service_prepare", {
        "slug": slug,
        "coverImageUrl": cover_url
    })
    draft_id = prep.get("draftId")
    if not draft_id:
        print(f"Prepare response: {prep}")
        return
    conf = call_tool("update_productized_service_confirm", {"confirm": True, "draftId": draft_id})
    print(f"✓ Service Cover Updated!")

def main():
    # 1. Product 2: Hardened CentOS Stream 10 Baseline
    product_centos = {
        "title": "Hardened CentOS Stream 10 & Podman Production Baseline",
        "description": "A turnkey, production-grade operating system baseline and container runtime architecture designed for mission-critical enterprise workloads. Engineered according to strict EVALinux hardening standards, CIS Linux Benchmarks, and Red Hat Enterprise Linux best practices.\n\nPackage your bare-metal servers and cloud instances with automated provisioning, zero-trust network perimeter controls, mandatory SELinux Enforcing posture, and declarative systemd Quadlets.\n\n### What's Included\n1. **Automated Kickstart Provisioning**: Declarative Anaconda Kickstart profile for unattended CentOS Stream 10 installations with encrypted LVM partitioning.\n2. **Defense-in-Depth System Hardening**: Mandatory SELinux Enforcing policies, hardened sysctl network stack tuning, and restricted SSH configurations.\n3. **Rootless Podman & systemd Quadlets**: Complete architecture for daemonless, rootless container execution with auto-restart policies and structured journald logging.\n4. **Automated Security Audit Suite**: Lightweight OpenSCAP compliance scanning scripts and drift detection tools.",
        "coverImageUrl": "https://raw.githubusercontent.com/renich/contra/main/assets/diagrams/modelyo-openstack-gcp.png?v=product2",
        "offerings": [
            {
                "title": "Production Baseline Toolkit",
                "price": "195.00",
                "description": "Instant access to the private repository containing all Kickstart profiles, Ansible roles, Quadlet templates, and compliance verification scripts.",
                "postPurchaseDetails": "Thank you for your purchase. You receive direct access to the private EVALinux Hardened CentOS Stream 10 Baseline repository: https://github.com/evalinux/centos-stream-10-baseline (or contact renich@evalinux.com with your GitHub/GitLab username for immediate invite access). Support inquiries: renich@evalinux.com."
            }
        ],
        "publish": True
    }

    # 2. Product 3: Sovereign Forgejo Kit
    product_forgejo = {
        "title": "Sovereign Forgejo & CI/CD Runner Platform Kit",
        "description": "A production-ready, declarative deployment blueprint for hosting your own ultra-secure Git forge and containerized CI/CD runner fleet on CentOS Stream 10. Eliminate SaaS per-seat license fees ($21–$99/user/month), maintain 100% intellectual property privacy, and run automated pipelines on your own bare-metal or cloud infrastructure.\n\nThis complete engineering kit packages rootless Podman Quadlet definitions, PostgreSQL database configurations, automated TLS reverse proxying, and secure runner daemon sandboxes.\n\n### What's Included\n1. **Declarative Podman Quadlet Stack**: Native systemd Quadlet files for rootless Forgejo, PostgreSQL, and Caddy with automatic lifecycle management.\n2. **Isolated Act Runner Fleet**: Hardened Forgejo Runner configuration running in rootless Podman mode with local build caching and resource limits.\n3. **Hardened Security & Identity Baseline**: SELinux Enforcing policies, automated Let's Encrypt TLS reverse proxying, and OAuth2/LDAP configuration templates.\n4. **Disaster Recovery Automation**: Automated daily snapshot and encrypted backup scripts with one-command point-in-time recovery.",
        "coverImageUrl": "https://raw.githubusercontent.com/renich/contra/main/assets/diagrams/advantagemls-gcp.png?v=product3",
        "offerings": [
            {
                "title": "Turnkey Deployment Blueprint & Quadlets",
                "price": "149.00",
                "description": "Instant access to the private repository containing all Quadlet definitions, automation scripts, workflow examples, and administrator guide.",
                "postPurchaseDetails": "Thank you for your purchase. You receive direct access to the private EVALinux Sovereign Forgejo Platform Kit repository: https://github.com/evalinux/forgejo-runner-kit (or contact renich@evalinux.com with your GitHub/GitLab username for immediate invite access). Support inquiries: renich@evalinux.com."
            }
        ],
        "publish": True
    }

    publish_product(product_centos)
    publish_product(product_forgejo)

    # Update covers for services
    update_service_cover(
        "7vW66W2v-sovereign-git-forge-and-cicd-runner-platform-deployment",
        "https://raw.githubusercontent.com/renich/contra/main/assets/diagrams/advantagemls-gcp.png?v=service-git-forge"
    )
    update_service_cover(
        "FocA2qgU-v-mware-virtualization-rescue-sovereign-kvm-and-ceph-migration",
        "https://raw.githubusercontent.com/renich/contra/main/assets/diagrams/cloudsigma-kvm.png?v=service-vmware-rescue"
    )

if __name__ == "__main__":
    main()
