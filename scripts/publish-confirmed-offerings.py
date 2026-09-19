#!/usr/bin/env python3
"""
scripts/publish-confirmed-offerings.py
Publishes confirmed productized services and digital products to Contra via JSON-RPC MCP.
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

def publish_service(data):
    print(f"\n--- Preparing Service: {data['title']} ---")
    prep = call_tool("create_productized_service_prepare", data)
    draft_id = prep.get("draftId")
    if not draft_id:
        raise RuntimeError(f"Failed to prepare service: {prep}")
    print(f"Prepared! Draft ID: {draft_id}")
    print(f"--- Confirming Service: {data['title']} ---")
    conf = call_tool("create_productized_service_confirm", {"confirm": True, "draftId": draft_id})
    print(f"✓ Confirmed & Published! Slug: {conf.get('slug')}")
    print(f"  URL: {conf.get('serviceUrl')}")
    return conf

def publish_product(data):
    print(f"\n--- Preparing Digital Product: {data['title']} ---")
    prep = call_tool("create_product_prepare", data)
    draft_id = prep.get("draftId")
    if not draft_id:
        raise RuntimeError(f"Failed to prepare product: {prep}")
    print(f"Prepared! Draft ID: {draft_id}")
    print(f"--- Confirming Digital Product: {data['title']} ---")
    conf = call_tool("create_product_confirm", {"confirm": True, "draftId": draft_id})
    print(f"✓ Confirmed & Published! Slug: {conf.get('slug')}")
    print(f"  URL: {conf.get('productUrl')}")
    return conf

def main():
    # 1. Service: Sovereign Git Forge
    service_git_forge = {
        "title": "Sovereign Git Forge & CI/CD Runner Platform Deployment",
        "description": "Eliminate escalating per-seat SaaS fees ($21–$99/user/month on GitHub Enterprise or GitLab SaaS), prevent proprietary source code and algorithms from commercial AI model ingestion, and achieve total developer infrastructure sovereignty.\n\nWe deploy, configure, and harden a turnkey, self-hosted Git platform powered by **Forgejo** and containerized **Act Runner CI/CD fleets** running on **CentOS Stream 10** with native Podman Quadlets.\n\n### What Makes This Platform Unique\n* **Zero Per-Seat SaaS Tax**: Host unlimited developers, repositories, and CI/CD pipelines without recurring license bills.\n* **100% IP & Secret Privacy**: Your codebase remains strictly within your own air-gapped or private cloud perimeter.\n* **Extreme Performance & Low Footprint**: Forgejo's compiled Go engine delivers blazing response times with minimal RAM footprint compared to monolithic alternatives.\n* **Enterprise Security Baseline**: Hardened with SELinux Enforcing posture, rootless container isolation, and automated Let's Encrypt TLS.\n\n### Delivery Workflow\n1. **Requirements & Architecture Intake**: Review directory requirements, existing repos, and CI/CD workflow dependencies.\n2. **Platform & Database Hardening**: Provision CentOS Stream 10 host, configure PostgreSQL, and deploy Forgejo with systemd Quadlets.\n3. **CI/CD Runner Fleet Setup**: Deploy and sandbox Act Runner daemons for containerized pipeline execution.\n4. **Pilot Migration & SSO**: Validate repository imports, configure SSO/LDAP, and verify commit signing policies.\n5. **Operational Handover**: Deliver admin runbooks, verify automated daily backup restoration, and train your team.",
        "deliverables": [
            {
                "title": "Hardened Forgejo Deployment on CentOS Stream 10",
                "description": "Production Forgejo instance configured with rootless Podman Quadlets, dedicated PostgreSQL backend, automated daily backups, and automated TLS reverse proxying."
            },
            {
                "title": "Dedicated Containerized CI/CD Runner Fleet",
                "description": "Forgejo Runner daemon running in isolated rootless container sandboxes with dependency caching, resource limits, and GitHub Actions workflow compatibility."
            },
            {
                "title": "Zero-Trust Access & Repository Governance",
                "description": "SELinux Enforcing confinement, corporate SSO/LDAP/OIDC integration, branch protection enforcement, and mandatory signed commit verification."
            },
            {
                "title": "Backup Automation & Disaster Recovery Runbook",
                "description": "Encrypted off-site snapshot sync, verified point-in-time recovery procedure, and complete administrative operations documentation."
            }
        ],
        "duration": {"amount": 2, "interval": "WEEK"},
        "price": {"amount": 4000, "type": "FIXED_PRICE"},
        "tags": ["Linux", "DevOps Engineer", "CentOS", "Containers", "Security", "CI/CD", "PostgreSQL", "Git"],
        "relatedPortfolioProjectIds": [
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgyOV0=",
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgzMF0="
        ],
        "publish": True
    }

    # 2. Service: VMware Virtualization Rescue
    service_vmware_rescue = {
        "title": "VMware Virtualization Rescue: Sovereign KVM & Ceph Migration",
        "description": "Escape Broadcom's predatory 200% to 1,500% VMware license renewal price hikes, punitive per-core floors, and vSAN raw storage capacity taxes.\n\nWe deliver a battle-tested, 100% non-destructive migration pathway from VMware vSphere/ESXi to a sovereign virtualization platform powered by **Enterprise Linux (CentOS Stream 10), KVM/QEMU, and libvirt** (backed by **Ceph** distributed storage for multi-node clusters or **Software RAID** for lean 1–3 host environments).\n\n### Guaranteed Engineering Commitments\n* **Immediate Reversal in Under 60 Seconds**: Migration is strictly non-destructive. Source VMware virtual machines remain completely untouched as cold backups until final sign-off.\n* **Guaranteed 35%+ 3-Year Net TCO Savings**: Consolidated migration and operating costs beat VMware subscriptions by 35% to 79%.\n* **Zero Recurring Software License Fees**: The hypervisor software cost is **$0 USD forever**.\n* **Direct Principal Architecture**: Led by **Rénich Bon Ćirić** (RHCE), with 20+ years experience running 150,000+ VMs globally (CloudSigma) and federal-scale cloud migrations (ADIP).\n\n### Turnkey Delivery Workflow\n1. **Free Sizing & Feasibility Audit**: Workload inventory analysis from RVTools or vCenter exports with zero network intrusion.\n2. **Target Hypervisor Provisioning**: Deploy CentOS Stream 10, configure 10G/25G LACP network bonding, and tune KVM/libvirt.\n3. **Pilot Workload Migration**: Migrate 1–2 test workloads to validate VirtIO drivers and measure sync windows.\n4. **Controlled Phased Cutover**: Automated migration waves during planned windows with live validation and verified fallback checkpoints.\n5. **Operational Delivery & Handover**: Complete architecture runbooks, automated backups, and administrator training.",
        "deliverables": [
            {
                "title": "Pre-Migration Workload & TCO Savings Audit",
                "description": "Complete inventory analysis from RVTools/vCenter exports, sizing verification, VirtIO compatibility matrix, and financial 3-year TCO savings model."
            },
            {
                "title": "Target Hypervisor Fleet Deployment on CentOS Stream 10",
                "description": "Turnkey installation and tuning of KVM/QEMU, libvirt, LACP network bonding, Software RAID mdadm or Ceph JBOD storage, and SELinux Enforcing posture."
            },
            {
                "title": "100% Non-Destructive Phased VM Migration with Rollback Safety Net",
                "description": "Differential block sync cutover with guaranteed sub-60-second fallback to source VMware environment, preserving cold backups until formal sign-off."
            },
            {
                "title": "Production Operations Runbook & Admin Training",
                "description": "Comprehensive runbooks for live migrations without SAN, snapshot/backup automation, and hands-on operational training for your engineering team."
            }
        ],
        "duration": {"amount": 3, "interval": "WEEK"},
        "price": {"amount": 6500, "type": "FIXED_PRICE"},
        "tags": ["Linux", "DevOps Engineer", "KVM", "Ceph", "CentOS", "Virtualization", "Infrastructure", "Disaster Recovery"],
        "relatedPortfolioProjectIds": [
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgzMV0=",
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgyOF0="
        ],
        "publish": True
    }

    # 3. Product: VMware-to-KVM Toolkit
    product_vmware = {
        "title": "VMware-to-KVM Migration Blueprint & Automation Toolkit",
        "description": "The battle-tested engineering blueprint, migration orchestrator scripts, and operational runbooks used to migrate mission-critical virtualization workloads from VMware vSphere/ESXi to KVM/libvirt on CentOS Stream 10.\n\nBuilt for IT directors, systems administrators, and enterprise infrastructure engineers escaping Broadcom's predatory VMware renewal price hikes, this toolkit provides a repeatable, 100% non-destructive migration pipeline with a guaranteed sub-60-second rollback strategy.\n\n### What's Included\n1. **Pre-Migration Workload & TCO Sizing Calculator**: Automated spreadsheet model for RVTools/vCenter inventory analysis and financial TCO comparison.\n2. **Target Hypervisor Hardening Playbooks**: Ansible/Kickstart baselines for CentOS Stream 10 hypervisors with LACP bonding, hugepages tuning, and strict SELinux Enforcing policies.\n3. **Automated VM Conversion & Differential Sync Scripts**: Bash/Python orchestrator using `virt-v2v` with sparse allocation, VirtIO injection, and minimal cutover downtime.\n4. **Operations & Disaster Recovery Runbook**: Step-by-step procedures for live migrations without SAN arrays, automated snapshot/backup pipelines, and emergency rollback protocols.",
        "offerings": [
            {
                "title": "Complete Engineering Toolkit & Runbook",
                "price": "295.00",
                "description": "Full access to the private repository containing all migration scripts, sizing spreadsheets, Ansible playbooks, and disaster recovery runbooks.",
                "postPurchaseDetails": "Thank you for your purchase. You receive direct access to the private EVALinux VMware-to-KVM Migration Toolkit repository. Clone the repository and review docs/quickstart.rst to begin: https://github.com/evalinux/vmware-to-kvm-toolkit (or contact renich@evalinux.com with your GitHub/GitLab username for immediate invite access). Support inquiries: renich@evalinux.com."
            }
        ],
        "publish": True
    }

    # 4. Product: Hardened CentOS Stream 10 Baseline
    product_centos = {
        "title": "Hardened CentOS Stream 10 & Podman Production Baseline",
        "description": "A turnkey, production-grade operating system baseline and container runtime architecture designed for mission-critical enterprise workloads. Engineered according to strict EVALinux hardening standards, CIS Linux Benchmarks, and Red Hat Enterprise Linux best practices.\n\nPackage your bare-metal servers and cloud instances with automated provisioning, zero-trust network perimeter controls, mandatory SELinux Enforcing posture, and declarative systemd Quadlets.\n\n### What's Included\n1. **Automated Kickstart Provisioning**: Declarative Anaconda Kickstart profile for unattended CentOS Stream 10 installations with encrypted LVM partitioning.\n2. **Defense-in-Depth System Hardening**: Mandatory SELinux Enforcing policies, hardened sysctl network stack tuning, and restricted SSH configurations.\n3. **Rootless Podman & systemd Quadlets**: Complete architecture for daemonless, rootless container execution with auto-restart policies and structured journald logging.\n4. **Automated Security Audit Suite**: Lightweight OpenSCAP compliance scanning scripts and drift detection tools.",
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

    # 5. Product: Sovereign Forgejo Kit
    product_forgejo = {
        "title": "Sovereign Forgejo & CI/CD Runner Platform Kit",
        "description": "A production-ready, declarative deployment blueprint for hosting your own ultra-secure Git forge and containerized CI/CD runner fleet on CentOS Stream 10. Eliminate SaaS per-seat license fees ($21–$99/user/month), maintain 100% intellectual property privacy, and run automated pipelines on your own bare-metal or cloud infrastructure.\n\nThis complete engineering kit packages rootless Podman Quadlet definitions, PostgreSQL database configurations, automated TLS reverse proxying, and secure runner daemon sandboxes.\n\n### What's Included\n1. **Declarative Podman Quadlet Stack**: Native systemd Quadlet files for rootless Forgejo, PostgreSQL, and Caddy with automatic lifecycle management.\n2. **Isolated Act Runner Fleet**: Hardened Forgejo Runner configuration running in rootless Podman mode with local build caching and resource limits.\n3. **Hardened Security & Identity Baseline**: SELinux Enforcing policies, automated Let's Encrypt TLS reverse proxying, and OAuth2/LDAP configuration templates.\n4. **Disaster Recovery Automation**: Automated daily snapshot and encrypted backup scripts with one-command point-in-time recovery.",
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

    print("==================================================")
    print("Publishing Confirmed Offerings to Contra.com")
    print("==================================================")

    publish_service(service_git_forge)
    publish_service(service_vmware_rescue)
    publish_product(product_vmware)
    publish_product(product_centos)
    publish_product(product_forgejo)

    print("\n==================================================")
    print("All 5 offerings published successfully!")
    print("==================================================")

if __name__ == "__main__":
    main()
