#!/usr/bin/env python3
"""
scripts/prepare-banner-updates.py - Prepares cover image updates for all 11 services and 4 portfolio projects.
Outputs human-readable preview changes compliant with Contra safety rules.
"""

import sys
import json
import urllib.request
import urllib.error

sys.path.insert(0, "scripts")
import contra_cli

SERVICES_MAP = [
    {
        "slug": "FocA2qgU-v-mware-virtualization-rescue-sovereign-kvm-and-ceph-migration",
        "title": "VMware Virtualization Rescue: Sovereign KVM & Ceph Migration",
        "banner": "service-vmware-rescue.jpg"
    },
    {
        "slug": "POXsvYUQ-autonomous-ai-and-agent-workflow-integration",
        "title": "Autonomous AI & Agent Workflow Integration",
        "banner": "service-ai-agent.jpg"
    },
    {
        "slug": "Xbg7ALqN-hardened-linux-and-container-infrastructure",
        "title": "Hardened Linux & Container Infrastructure",
        "banner": "service-hardened-linux.jpg"
    },
    {
        "slug": "QbN6svWo-high-availability-database-cluster-deployment-and-hardening",
        "title": "High-Availability Database Cluster Deployment & Hardening",
        "banner": "service-ha-db.jpg"
    },
    {
        "slug": "rLYsZ2vY-cloud-fin-ops-and-infrastructure-cost-optimization-sprint",
        "title": "Cloud FinOps & Infrastructure Cost Optimization Sprint",
        "banner": "service-cloud-finops.jpg"
    },
    {
        "slug": "QocPNgeg-zero-trust-remote-access-and-identity-aware-architecture",
        "title": "Zero-Trust Remote Access & Identity-Aware Architecture",
        "banner": "service-zero-trust.jpg"
    },
    {
        "slug": "7vW66W2v-sovereign-git-forge-and-cicd-runner-platform-deployment",
        "title": "Sovereign Git Forge & CI/CD Runner Platform Deployment",
        "banner": "service-git-forge.jpg"
    },
    {
        "slug": "r6k2QLPl-production-observability-and-sre-telemetry-platform",
        "title": "Production Observability & SRE Telemetry Platform",
        "banner": "service-observability.jpg"
    },
    {
        "slug": "62m2YcOk-infrastructure-and-cloud-architecture-audit",
        "title": "Infrastructure & Cloud Architecture Audit",
        "banner": "service-audit.jpg"
    },
    {
        "slug": "vRLNmF6g-sovereign-enterprise-mail-server-and-exu-suite-deployment",
        "title": "Sovereign Enterprise Mail Server & exu Suite Deployment",
        "banner": "service-exu-mail.jpg"
    },
    {
        "slug": "BcYboLNL-fractional-principal-sre-and-platform-architect",
        "title": "Fractional Principal SRE & Platform Architect",
        "banner": "service-fractional-sre.jpg"
    }
]

PROJECTS_MAP = [
    {
        "slug": "MlPbONqF-enterprise-cloud-migration-4500-instances-to-open-stack",
        "title": "Enterprise Cloud Migration: 4500 Instances to OpenStack",
        "banner": "case-adip-migration.jpg"
    },
    {
        "slug": "6ZNWPseo-dollar45kyr-cloud-cost-optimization-and-zero-downtime-os-upgrade",
        "title": "$45k/Yr Cloud Cost Optimization & Zero-Downtime OS Upgrade",
        "banner": "case-advantagemls-gcp.jpg"
    },
    {
        "slug": "2YFqb7UL-scaling-global-virtualization-to-150k-v-ms-and-s3-storage",
        "title": "Scaling Global Virtualization to 150k+ VMs & S3 Storage",
        "banner": "case-cloudsigma-kvm.jpg"
    },
    {
        "slug": "YMEcRWYm-ha-open-stack-control-plane-on-google-cloud-platform",
        "title": "HA OpenStack Control Plane on Google Cloud Platform",
        "banner": "case-modelyo-openstack.jpg"
    }
]

CDN_BASE = "https://raw.githubusercontent.com/renich/contra/main/assets/banners"

def main():
    prepared_data = {
        "services": [],
        "projects": []
    }

    print("=== PREPARING SERVICE BANNER UPDATES ===")
    for item in SERVICES_MAP:
        url = f"{CDN_BASE}/{item['banner']}"
        print(f"Preparing service: {item['title']}...")
        res = contra_cli.call_tool("update_productized_service_prepare", {
            "slug": item["slug"],
            "coverImageUrl": url
        })
        sc = res.get("result", {}).get("structuredContent", {})
        if not sc.get("ok"):
            print(f"FAILED: {res}")
            sys.exit(1)
        item["draftId"] = sc.get("draftId")
        item["changes"] = sc.get("preview", {}).get("changes", [])
        item["serviceUrl"] = sc.get("preview", {}).get("serviceUrl")
        item["warning"] = sc.get("preview", {}).get("warning")
        prepared_data["services"].append(item)

    print("\n=== PREPARING CASE STUDY BANNER UPDATES ===")
    for item in PROJECTS_MAP:
        url = f"{CDN_BASE}/{item['banner']}"
        print(f"Preparing project: {item['title']}...")
        res = contra_cli.call_tool("update_portfolio_project_prepare", {
            "slug": item["slug"],
            "coverImageUrl": url
        })
        sc = res.get("result", {}).get("structuredContent", {})
        if not sc.get("ok"):
            print(f"FAILED: {res}")
            sys.exit(1)
        item["draftId"] = sc.get("draftId")
        item["changes"] = sc.get("preview", {}).get("changes", [])
        item["projectUrl"] = sc.get("preview", {}).get("projectUrl")
        item["warning"] = sc.get("preview", {}).get("warning")
        prepared_data["projects"].append(item)

    with open("prepared-banner-drafts.json", "w") as f:
        json.dump(prepared_data, f, indent=2)

    print("\nAll 15 drafts prepared successfully and saved to prepared-banner-drafts.json!")

if __name__ == "__main__":
    main()
