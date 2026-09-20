#!/usr/bin/env python3
"""
scripts/prepare-new-services.py
Prepares 5 new productized services on Contra MCP and prints previews.
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

def main():
    services = [
        {
            "title": "Cloud FinOps & Infrastructure Cost Optimization Sprint",
            "description": "Slash escalating monthly cloud expenditures by 25% to 40%, eliminate waste, and establish reproducible cost governance without compromising system performance or reliability.\n\nBacked by verified real-world outcomes (including slashing AdvantageMLS's annual Google Cloud Platform spend by **$45,000+**), we execute a targeted, 2-week engineering sprint analyzing p99 utilization metrics, eliminating idle and orphaned cloud resources, re-architecting expensive network data egress, and converting legacy infrastructure into modular, drift-controlled **OpenTofu** code.\n\n### Why Cloud Cost Optimization?\n* **Immediate Positive ROI**: Typical cloud optimizations generate $20,000 to $100,000+ in annualized savings, frequently paying for this sprint within the first 60 to 90 days.\n* **Architectural Rightsizing**: We do not merely cut instance sizes blindly; we analyze real-world p99 CPU, memory, and disk IOPS utilization to rightsize machine families safely.\n* **Network Egress Optimization**: Network data transfer between cloud zones, regions, and to the public internet is often an invisible financial drain. We redesign CDN edge rules and internal routing to slash egress fees.\n* **Infrastructure as Code Baseline**: Ensure cost savings remain permanent by codifying the optimized infrastructure in clean, modular OpenTofu/Terraform modules with automated drift detection.",
            "deliverables": [
                {"title": "Deep-Dive Cloud Spend & Utilization Audit", "description": "Comprehensive billing analysis, orphaned disk/snapshot detection, and p99 compute profiling."},
                {"title": "Compute Rightsizing & Ephemeral Automation", "description": "Workload migration to cost-effective machine families and automated off-hours shutdown playbooks."},
                {"title": "CDN Edge Caching & Egress Slicing Architecture", "description": "Re-engineered CDN caching rules and private VPC routing to slash data transfer egress fees."},
                {"title": "Declarative OpenTofu IaC & Cost Guardrails", "description": "Modular OpenTofu codebase with automated budget alert triggers and drift detection."}
            ],
            "duration": {"amount": 2, "interval": "WEEK"},
            "price": {"amount": 4500, "type": "FIXED_PRICE"},
            "tags": ["Google Cloud Platform", "Terraform", "DevOps Engineer", "Cloud Architecture", "Linux", "Cost Optimization"],
            "relatedPortfolioProjectIds": ["WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgyOV0="],
            "coverImageUrl": "https://raw.githubusercontent.com/renich/contra/main/assets/diagrams/advantagemls-gcp.png?v=service-finops",
            "publish": True
        },
        {
            "title": "High-Availability Database Cluster Deployment & Hardening",
            "description": "Eliminate database single points of failure, prevent costly application outages during hardware failures or maintenance windows, and ensure verifiable zero data loss.\n\nWe architect, deploy, and benchmark high-availability database clusters powered by **PostgreSQL** (with **Patroni**, **pgBouncer**, and **WAL-G**) or **MariaDB Galera** synchronous multi-master clusters on hardened **CentOS Stream 10**. Every deployment includes sub-second automated failover, connection pooling, continuous streaming backups, and verified point-in-time recovery (PITR).\n\n### Why Professional HA Database Clustering?\n* **Zero-Downtime Maintenance**: Perform operating system upgrades, security patches, and hardware replacements on individual nodes without taking your application offline.\n* **Sub-Second Automated Failover**: Distributed consensus agents detect node or network failures and promote healthy replicas instantaneously without manual intervention.\n* **Connection Pooling & Query Routing**: Decouple application connection spikes from backend database worker limits using high-performance connection pooling.\n* **Verifiable Disaster Recovery**: Continuous transaction log streaming to S3-compatible object storage with automated point-in-time recovery drills.",
            "deliverables": [
                {"title": "Multi-Node Synchronous Database Cluster", "description": "PostgreSQL with Patroni/etcd consensus or MariaDB Galera multi-master on CentOS Stream 10 with sub-second automated failover."},
                {"title": "Connection Pooling & Intelligent Load Balancing", "description": "pgBouncer or HAProxy with transaction-level pooling and read/write query splitting."},
                {"title": "Continuous Streaming Backups & Point-in-Time Recovery", "description": "Continuous WAL archiving to S3, daily snapshots, and verified point-in-time recovery drill."},
                {"title": "Kernel & Storage Performance Hardening", "description": "Linux kernel sysctl tuning, shared memory optimization, and strict SELinux Enforcing posture."}
            ],
            "duration": {"amount": 2, "interval": "WEEK"},
            "price": {"amount": 5000, "type": "FIXED_PRICE"},
            "tags": ["PostgreSQL", "Linux", "DevOps Engineer", "Database", "High Availability", "CentOS", "MariaDB", "Disaster Recovery"],
            "relatedPortfolioProjectIds": ["WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgzMV0=", "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgyOF0="],
            "coverImageUrl": "https://raw.githubusercontent.com/renich/contra/main/assets/diagrams/cloudsigma-kvm.png?v=service-db",
            "publish": True
        },
        {
            "title": "Zero-Trust Remote Access & Identity-Aware Architecture",
            "description": "Eliminate vulnerable, slow, and brittle perimeter VPN appliances (OpenVPN, Cisco AnyConnect, Pulse Secure), prevent ransomware lateral movement across internal networks, and establish continuous identity-aware access control.\n\nWe design and implement a modern, enterprise-grade **Zero-Trust Architecture** based on **Identity-Aware Proxies (IAP)**, **WireGuard peer-to-peer mesh networks**, and **mutual TLS (mTLS)** micro-segmentation running on hardened **CentOS Stream 10**. Remote developers and internal staff securely access corporate applications and administrative consoles through standard web browsers backed by enterprise Multi-Factor Authentication (MFA), without exposing a single open ingress VPN port to the public internet.\n\n### Why Move Beyond Traditional VPNs?\n* **Eliminate Lateral Movement**: Traditional VPNs place authenticated devices directly onto the corporate subnet, allowing a single compromised laptop to scan and infect your entire infrastructure. Zero Trust enforces least-privilege access per application.\n* **Frictionless Browser-Based Access**: Internal tools (dashboards, admin portals, Git forges, monitoring) are accessible directly via web browsers authenticated via corporate SSO/MFA, eliminating client software deployment headaches.\n* **Stealth Public Perimeters**: Remove public-facing VPN listeners. All inbound connections are authenticated and authorized cryptographically before reaching internal network services.\n* **Micro-Segmented Workload Isolation**: Service-to-service traffic between servers and containers is strictly encrypted and verified via mTLS or WireGuard overlays.",
            "deliverables": [
                {"title": "Identity-Aware Proxy (IAP) Deployment", "description": "Browser-based access to internal tools authenticated via corporate SSO/MFA without traditional VPNs."},
                {"title": "Peer-to-Peer WireGuard Mesh & Micro-Segmentation", "description": "Encrypted WireGuard mesh between production servers with strict network micro-segmentation."},
                {"title": "Mutual TLS (mTLS) Service Hardening", "description": "Private Certificate Authority infrastructure enforcing cryptographic workload identity."},
                {"title": "Defense-in-Depth Host Hardening & Firewall Rules", "description": "Restrictive firewalld zones, closed public VPN listener ports, and mandatory SELinux Enforcing posture."}
            ],
            "duration": {"amount": 2, "interval": "WEEK"},
            "price": {"amount": 4500, "type": "FIXED_PRICE"},
            "tags": ["Security", "Linux", "DevOps Engineer", "Zero Trust", "WireGuard", "Infrastructure", "mTLS", "CentOS"],
            "relatedPortfolioProjectIds": ["WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgzMF0="],
            "coverImageUrl": "https://raw.githubusercontent.com/renich/contra/main/assets/diagrams/modelyo-openstack-gcp.png?v=service-zerotrust",
            "publish": True
        },
        {
            "title": "Production Observability & SRE Telemetry Platform",
            "description": "Escape extortionate SaaS observability bills ($5,000–$20,000+/month on Datadog or New Relic), eliminate metric noise and unhelpful alert spam, and gain crystal-clear visibility into production health.\n\nWe architect and deploy a production-grade, sovereign telemetry stack powered by **Prometheus**, **Grafana**, and **Alertmanager** on **CentOS Stream 10**. We replace hundreds of noisy alerts with actionable Service Level Objectives (SLOs) focused on the **Four Golden Signals** (Latency, Traffic, Errors, and Saturation), with high-priority notifications routed directly to PagerDuty, Slack, or Telegram.\n\n### Why Sovereign Observability?\n* **Zero Per-Host SaaS Penalties**: SaaS vendors bill exponentially for every new container, host, and custom metric. A self-hosted Prometheus/Grafana architecture handles millions of samples per second on your own hardware without licensing fees.\n* **Signal Over Noise**: Drowning in false-positive alerts causes operational burnout and missed real outages. We implement mathematically grounded multi-window SLO burn-rate alerts that fire only when user experience is genuinely compromised.\n* **High-Performance Long-Term Metrics**: Retention tuning, efficient downsampling, and disk compression keeping months of historical telemetry accessible in seconds.\n* **Unified Fleet Telemetry**: Complete visibility across physical bare-metal nodes, virtual hypervisors, container workloads, and network interfaces.",
            "deliverables": [
                {"title": "Production Prometheus & Alertmanager Architecture", "description": "Multi-target metric scraping, high-cardinality storage, and retention tuning on CentOS Stream 10."},
                {"title": "Executive & Engineering Grafana Dashboards", "description": "Visualization of the Four Golden Signals: latency, traffic, errors, and saturation with synthetic endpoint monitoring."},
                {"title": "Structured Logging & Journald Telemetry", "description": "Hardened systemd-journald structured JSON logging with fast querying and automated rotation."},
                {"title": "Actionable Alert Routing & Incident Response Integration", "description": "Multi-window SLO burn-rate alerting routed to PagerDuty/Slack/Telegram eliminating false positives."}
            ],
            "duration": {"amount": 2, "interval": "WEEK"},
            "price": {"amount": 3500, "type": "FIXED_PRICE"},
            "tags": ["Prometheus", "Grafana", "Linux", "DevOps Engineer", "Site Reliability Engineering", "Observability", "CentOS"],
            "relatedPortfolioProjectIds": ["WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgzMV0="],
            "coverImageUrl": "https://raw.githubusercontent.com/renich/contra/main/assets/diagrams/cloudsigma-kvm.png?v=service-obs",
            "publish": True
        },
        {
            "title": "Sovereign Enterprise Mail Server & exu Suite Deployment",
            "description": "Escape recurring per-user SaaS license fees ($6–$30/user/month on Microsoft 365 or Google Workspace), retain absolute data sovereignty over executive correspondence, and eliminate email deliverability failures.\n\nWe deploy and harden a sovereign, high-deliverability enterprise mail infrastructure powered by **EVALinux exu Suite**, **Exim**, **Dovecot**, and **Caddy** on **CentOS Stream 10**. Built with a statically compiled Crystal daemon and CLI, `exu` provides an intuitive Single-Page Application (SPA) web control plane protected by client-certificate mTLS authentication, alongside native command-line administration (`eum`), automated 2048-bit DKIM key generation, and copy-paste ready DNS records for a guaranteed **10/10 deliverability score**.\n\n### Why Sovereign Enterprise Mail with exu?\n* **Zero Per-Seat SaaS Taxes**: Host unlimited domains, mailboxes, and aliases on your private server infrastructure without recurring per-inbox fees.\n* **100% Data Privacy & Legal Sovereignty**: Retain full ownership of corporate email archives, protected from automated cloud scanning and foreign legal jurisdiction.\n* **Guaranteed 10/10 Deliverability**: Perfect inbox placement backed by automated RSA-2048 DKIM signing, strict SPF alignment, DMARC enforcement, and verified rDNS/PTR configuration.\n* **Bank-Grade Security**: Decoupled transport mTLS client certificate authentication with encrypted HMAC-SHA256 session cookies, POSIX advisory locking, and non-invasive modular MTA configuration files.",
            "deliverables": [
                {"title": "Turnkey exu Virtual Mail Suite Deployment", "description": "Statically compiled exu daemon, eum CLI, Exim MTA, and Dovecot IMAP/POP3 on CentOS Stream 10."},
                {"title": "Web Control Dashboard & mTLS Authentication", "description": "Modern SPA web administration portal secured by client-certificate mTLS authentication."},
                {"title": "Complete Deliverability & Cryptographic DNS Baseline", "description": "Automated 2048-bit DKIM key rotation, strict SPF, DMARC alignment, and verified 10/10 deliverability."},
                {"title": "Virtual Domains, Multi-Recipient Aliases & Autodiscover", "description": "Multi-domain hosting, auto-seeded alias templates, and Thunderbird/Outlook autodiscover protocols."}
            ],
            "duration": {"amount": 1, "interval": "WEEK"},
            "price": {"amount": 3000, "type": "FIXED_PRICE"},
            "tags": ["Linux", "DevOps Engineer", "CentOS", "Email", "Security", "Crystal", "DNS", "Caddy"],
            "relatedPortfolioProjectIds": ["WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgzMV0=", "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgyOF0="],
            "coverImageUrl": "https://raw.githubusercontent.com/renich/contra/main/assets/diagrams/adip-migration.png?v=service-mail",
            "publish": True
        }
    ]

    prepared_drafts = []
    for s in services:
        print(f"\nPreparing: {s['title']} ...")
        res = call_tool("create_productized_service_prepare", s)
        prepared_drafts.append({
            "title": s["title"],
            "draftId": res.get("draftId"),
            "summary": res.get("preview", {}).get("summary", [])
        })
        print(f"Draft ID: {res.get('draftId')}")

    with open("prepared_drafts.json", "w") as f:
        json.dump(prepared_drafts, f, indent=2)
    print("\nSaved prepared drafts to prepared_drafts.json")

if __name__ == "__main__":
    main()
