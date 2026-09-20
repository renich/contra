#!/usr/bin/env python3
"""
scripts/prepare-5-new-services.py - Prepares the 5 newly requested enterprise services on Contra.
"""

import sys
import json

sys.path.insert(0, "scripts")
import contra_cli

CDN_BASE = "https://raw.githubusercontent.com/renich/contra/main/assets/banners"

NEW_SERVICES = [
    {
        "title": "Enterprise RPM Packaging, GPG Signing & Automated DNF Repositories",
        "price": {
            "amount": 4000,
            "type": "FIXED_PRICE"
        },
        "duration": {
            "amount": 1,
            "interval": "WEEK"
        },
        "coverImageUrl": f"{CDN_BASE}/service-rpm-dnf.jpg",
        "publish": True,
        "tags": ["Linux", "CentOS", "DevOps Engineer", "CI/CD", "Security", "Automation", "GitLab"],
        "relatedPortfolioProjectIds": [
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgyOV0=", # AdvantageMLS
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgyOF0="  # ADIP
        ],
        "description": """Eliminate chaotic manual software installations, unverified binaries, and dependency drift across your Linux server fleet.

We engineer institutional-grade **RPM packaging pipelines**, automated **GPG package signing**, and high-availability **DNF/YUM repository distribution architectures**. Whether you need to distribute proprietary in-house applications, custom-patched open-source utilities, or complex polyglot runtimes, we transform your software delivery into reproducible, auditable, and immutable RPM artifacts seamlessly consumable by native `dnf` and `yum` package managers.

### Why Enterprise RPM Packaging & Managed Repositories?
* **Tamper-Proof Cryptographic Verification**: Every built RPM package and repository metadata catalog is signed with dedicated 4096-bit RSA or Ed25519 GPG keys, guaranteeing origin authenticity and file integrity before installation.
* **Isolated Reproducible Sandboxes**: Clean chroot build execution via Mock and Koji build systems prevents environmental pollution, undocumented build dependencies, and host leaks.
* **Native OS Lifecycle Management**: Clean integration with systemd unit files, SELinux policy contexts, user/group lifecycle scripts, and atomic rollback workflows.
* **High-Speed Mirrored Distribution**: Low-latency repository distribution via hardened Nginx or Caddy servers with automated delta-RPM generation and multi-node rsync replication.
""",
        "deliverables": [
            {
                "title": "Production-Grade RPM Spec Files",
                "description": "Standards-compliant RPM spec files authored according to Fedora and Red Hat packaging guidelines, with granular dependency trees, FHS 3.0 directory compliance, and declarative systemd scriptlets."
            },
            {
                "title": "Clean Chroot Build Pipeline (Mock & Koji)",
                "description": "Automated build configuration files for Mock and Koji enabling clean-room chroot builds across target distributions and architectures (x86_64, aarch64), integrated with GitLab CI or GitHub Actions."
            },
            {
                "title": "Cryptographic GPG Signing Architecture",
                "description": "Dedicated 4096-bit packaging GPG key generation with secure sub-key separation, automated unattended CI signing integration using rpmsign, and branded bootstrap release RPMs."
            },
            {
                "title": "High-Availability DNF/YUM Repository & Mirroring",
                "description": "Automated metadata generation using createrepo_c with repomd XML signing, hardened Nginx/Caddy TLS web delivery, and automated multi-region rsync synchronization pipelines."
            }
        ],
        "faqs": [
            {
                "question": "Which Linux distributions are supported?",
                "answer": "We support Fedora, RHEL (8, 9, 10), CentOS Stream, Rocky Linux, and AlmaLinux across x86_64 and aarch64 architectures."
            },
            {
                "question": "How is signing key security handled in CI/CD pipelines?",
                "answer": "GPG private signing keys are never stored in raw repository files. We utilize dedicated signing sub-keys injected via masked CI secrets, HashiCorp Vault, or offline signing daemons with strict least-privilege permissions."
            }
        ]
    },
    {
        "title": "Enterprise FreeIPA HA & Centralized PKI/CA Infrastructure",
        "price": {
            "amount": 5500,
            "type": "FIXED_PRICE"
        },
        "duration": {
            "amount": 2,
            "interval": "WEEK"
        },
        "coverImageUrl": f"{CDN_BASE}/service-freeipa-pki.jpg",
        "publish": True,
        "tags": ["Linux", "Security", "DevOps Engineer", "DNS", "Automation", "Architecture"],
        "relatedPortfolioProjectIds": [
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgyOF0=", # ADIP
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgzMV0="  # CloudSigma
        ],
        "description": """Fragmented user accounts, scattered SSH keys, unmanaged sudo privileges, and expired TLS certificates represent the largest operational security liabilities in modern infrastructure.

We deploy a production-hardened, multi-master **High-Availability (HA) FreeIPA / Red Hat Identity Management (IdM)** domain combined with a multi-tier **Public Key Infrastructure (PKI)**. This unified sovereign architecture delivers centralized identity management, Kerberos Single Sign-On (SSO), Host-Based Access Control (HBAC), automated host certificate issuance, and centralized sudo governance across your entire Linux server fleet.

### Why Enterprise FreeIPA & Centralized Identity?
* **Zero Identity Fragmentation**: Single authoritative directory for user credentials, SSH public keys, groups, and netgroups across all hybrid cloud and bare-metal nodes.
* **Granular Host & Command Governance**: Fine-grained Host-Based Access Control (HBAC) and centralized sudo rule evaluation enforced natively by System Security Services Daemon (SSSD).
* **Multi-Master Replication & Zero Downtime**: Active-active directory topologies with multi-master LDAP and Kerberos replication, automated conflict resolution, and integrated DNS failover.
* **Automated Certificate Lifecycle**: Integrated Dogtag Certificate System with automated host/service TLS certificate enrollment and renewal via `certmonger` and ACME endpoints.
""",
        "deliverables": [
            {
                "title": "Multi-Master High-Availability FreeIPA Domain",
                "description": "Deployment of a minimum 2-node or 3-node HA FreeIPA topology with multi-master replication across availability zones, encrypted LDAPS transport, and automated disaster recovery playbooks."
            },
            {
                "title": "Centralized PKI Architecture & Sub-CA Management",
                "description": "Full deployment of Dogtag Certificate System integrated into FreeIPA, hierarchical Root/Sub-CA design, custom certificate profiles, automated CRL distribution, and OCSP responders."
            },
            {
                "title": "Automated Host Enrollment & SSSD Hardening",
                "description": "Idempotent client enrollment playbooks using official Ansible FreeIPA collections, hardened SSSD client configuration with offline caching, and certmonger tracking for zero-touch host certificate renewals."
            },
            {
                "title": "Role-Based Access Control, HBAC & Centralized Sudo",
                "description": "Granular user group hierarchy, administrative roles, strict Host-Based Access Control (HBAC) rules governing environment access, and centralized sudo command catalogs eliminating local sudoers drift."
            }
        ],
        "faqs": [
            {
                "question": "Can FreeIPA integrate with existing Active Directory (AD) domains?",
                "answer": "Yes. FreeIPA supports bi-directional and cross-forest Kerberos trusts with Microsoft Active Directory, allowing corporate AD users to authenticate seamlessly to Linux hosts with native POSIX attributes."
            },
            {
                "question": "What happens if a FreeIPA master node fails?",
                "answer": "The multi-master topology replicates all LDAP directory, Kerberos KDC, and DNS records continuously. Clients automatically fail over to secondary replicas via SSSD domain priority and DNS SRV records with zero session interruption."
            }
        ]
    },
    {
        "title": "High-Availability Ingress & Hardened Reverse Proxies: HAProxy & Caddy",
        "price": {
            "amount": 3500,
            "type": "FIXED_PRICE"
        },
        "duration": {
            "amount": 1,
            "interval": "WEEK"
        },
        "coverImageUrl": f"{CDN_BASE}/service-ha-proxy.jpg",
        "publish": True,
        "tags": ["Linux", "Caddy", "DevOps Engineer", "Security", "Architecture", "Infrastructure"],
        "relatedPortfolioProjectIds": [
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgzMF0=", # Modelyo
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgyOV0="  # AdvantageMLS
        ],
        "description": """Ingress bottlenecks, ungraceful configuration reloads, single-point-of-failure load balancers, and flawed TLS setups degrade application performance and expose critical backend services to public exploitation.

We design and deploy high-throughput, resilient ingress gateways utilizing synchronized **HAProxy** and hardened **Caddy** reverse proxies. Backed by **Keepalived Virtual Router Redundancy Protocol (VRRP)** for sub-second IP failover, our edge architectures feature automated Let's Encrypt / ZeroSSL TLS certificate lifecycles, intelligent DDoS mitigation rate limiting, dynamic backend health probing, and hitless graceful configuration reloads.

### Why Enterprise Ingress with HAProxy & Caddy?
* **Sub-Second Failover & High Availability**: Redundant gateway pairs sharing Virtual IP (VIP) addresses via Keepalived ensure that host crashes or network drops trigger transparent, zero-downtime client failover.
* **Peak Layer-4 & Layer-7 Performance**: HAProxy handles millions of concurrent TCP/HTTP connections with sub-millisecond dispatch latencies and micro-architectural CPU affinity tuning.
* **Automated Modern Cryptography**: Caddy provides out-of-the-box, zero-maintenance automated TLS 1.3 certificates, HTTP/3 (QUIC) performance, and modern cipher suite negotiation.
* **Hitless Maintenance**: Zero-packet-drop runtime state synchronization and seamless reload mechanics ensure continuous uptime during configuration adjustments and security patching.
""",
        "deliverables": [
            {
                "title": "Redundant Active-Passive / Active-Active Gateway Cluster",
                "description": "Twin edge gateway nodes coordinated by Keepalived VRRP with track scripts, automated VIP promotion, Linux kernel network parameter tuning, and verified reboot failover."
            },
            {
                "title": "Production HAProxy Layer-4/7 Routing Engine",
                "description": "High-performance HAProxy deployment optimized for TCP and HTTP/2, advanced stick-tables for real-time DDoS rate limiting, dynamic health check probes, and runtime state preservation."
            },
            {
                "title": "Hardened Caddy Edge Proxy & Automated PKI",
                "description": "Automated TLS 1.3 termination using ACME protocols (Let's Encrypt / ZeroSSL), mutual TLS (mTLS) enforcement for administrative routes, and HTTP/3 QUIC acceleration."
            },
            {
                "title": "Telemetry, Structured Logging & Prometheus Metrics",
                "description": "Prometheus metrics export for HAProxy and Caddy tracking connection rates, error codes, queue latencies, structured syslog routing via journald, and alerting rules."
            }
        ],
        "faqs": [
            {
                "question": "Can this setup handle cloud environments that restrict VRRP multicast (like AWS or GCP)?",
                "answer": "Yes. In cloud environments where native Layer-2 VRRP/ARP broadcast is prohibited by SDN controllers, we deploy cloud-native internal load balancers with policy routing or unicast Keepalived tunnels to achieve identical sub-second failover."
            },
            {
                "question": "Do configuration reloads drop active user connections?",
                "answer": "No. We configure HAProxy seamless reloads (using socket transfer and hitless reload protocols) and Caddy zero-downtime reloads, ensuring zero connection drops during traffic spikes or certificate updates."
            }
        ]
    },
    {
        "title": "Custom Linux Distribution & Immutable OS Engineering: mkosi & UKI",
        "price": {
            "amount": 6000,
            "type": "FIXED_PRICE"
        },
        "duration": {
            "amount": 2,
            "interval": "WEEK"
        },
        "coverImageUrl": f"{CDN_BASE}/service-custom-os.jpg",
        "publish": True,
        "tags": ["Linux", "CentOS", "DevOps Engineer", "Security", "Architecture", "Infrastructure"],
        "relatedPortfolioProjectIds": [
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgzMV0=", # CloudSigma
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgyOF0="  # ADIP
        ],
        "description": """Traditional mutable operating systems suffer from configuration drift, silent package corruption, unauthorized tampering, and slow, non-deterministic recovery workflows.

We architect and build tailored, reproducible, and cryptographically verified Linux operating system distributions and appliances from source or upstream RPM repositories. Powered by modern **mkosi**, **Unified Kernel Images (UKIs)**, **systemd-repart**, and **dm-verity**, our immutable operating system images boot directly into read-only, cryptographically authenticated environments with hardware-backed TPM2 Secure Boot sealing, guaranteeing total platform integrity from bare-metal firmware to application runtimes.

### Why Custom Immutable Linux Distributions?
* **Zero Configuration Drift**: The root filesystem is strictly read-only and sealed with dm-verity hashes, ensuring that every deployment across edge, virtualization, or bare-metal is mathematically identical.
* **Tamper-Proof Boot Chain**: Unified Kernel Images (combining Linux kernel, initrd, and kernel cmdline into a single PE binary) signed with private SecureBoot keys and sealed to TPM2 PCR registers.
* **Atomic A/B Upgrades**: Dual-bank partition layouts orchestrated by `systemd-sysupdate` and `systemd-repart` provide instantaneous, fail-safe updates with automated fallback upon boot failure.
* **Modular System Extensions**: Granular customization and zero-reboot runtime extension delivery via signed `systemd-sysext` and `systemd-confext` images.
""",
        "deliverables": [
            {
                "title": "Declarative mkosi Build Pipeline",
                "description": "Comprehensive, version-controlled mkosi manifests defining distribution packages, kernel parameters, filesystem hierarchies, generating raw disk images, QCOW2 appliances, and ISO live boot media."
            },
            {
                "title": "Unified Kernel Image (UKI) Architecture & Signing",
                "description": "Synthesis of kernel, systemd-stub, initrd, and command line into a single signed UKI binary, private SecureBoot key hierarchy, and TPM2 PCR measurement sealing."
            },
            {
                "title": "Immutable dm-verity Root & Partition Engineering",
                "description": "Declarative partition schemes authored with systemd-repart supporting automatic disk growth, LUKS2 disk encryption, dm-verity integrity trees, and read-only root mount policies."
            },
            {
                "title": "Modular Extension Management & A/B Update System",
                "description": "Authoring of systemd-sysext overlay packages for modular updates, atomic differential OS updates via systemd-sysupdate, testing fixtures in QEMU/KVM, and CI/CD workflows."
            }
        ],
        "faqs": [
            {
                "question": "Where does persistent data live in an immutable operating system?",
                "answer": "We strictly separate stateless OS files from stateful data. The root filesystem (`/usr`) is strictly read-only and dm-verity protected, while stateful configuration and data reside on dedicated, encrypted `/var` and `/etc` overlay partitions."
            },
            {
                "question": "Can this be deployed to edge devices, virtual machines, and cloud instances?",
                "answer": "Yes. mkosi produces target artifacts for raw UEFI bare-metal disks, edge appliances, QCOW2 images for KVM/Proxmox/OpenStack, and cloud images for GCP or AWS."
            }
        ]
    },
    {
        "title": "Core Sovereign Network Services: BIND9 DNSSEC, Kea DHCP & Chrony NTP",
        "price": {
            "amount": 3500,
            "type": "FIXED_PRICE"
        },
        "duration": {
            "amount": 1,
            "interval": "WEEK"
        },
        "coverImageUrl": f"{CDN_BASE}/service-core-network.jpg",
        "publish": True,
        "tags": ["DNS", "Linux", "DevOps Engineer", "Security", "Infrastructure", "Architecture"],
        "relatedPortfolioProjectIds": [
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgzMV0=", # CloudSigma
            "WyJQb3J0Zm9saW9Qcm9qZWN0Iiw0NjQwNjgzMF0="  # Modelyo
        ],
        "description": """Flawed DNS resolution, fragile DHCP single points of failure, and unsynchronized system clocks cascade into catastrophic outages, broken TLS handshakes, distributed database split-brains, and invalid audit logs.

We engineer sovereign, enterprise-grade core network infrastructure built on the gold standards of Internet engineering: authoritative and recursive **BIND 9** with automated **DNSSEC** signing, high-throughput **Kea DHCP** with active-active High-Availability database clustering, and sub-millisecond precision **Chrony NTP** time synchronization. This triad provides the rock-solid, resilient foundation required for modern datacenter, campus, and hybrid cloud operations.

### Why Sovereign Core Network Infrastructure?
* **Cryptographic DNS Integrity**: BIND9 with automated DNSSEC key management (inline signing, KASP policies) protects internal and public zones against DNS cache poisoning, spoofing, and man-in-the-middle exploits.
* **Resilient Active-Active DHCP**: Kea DHCP with PostgreSQL/MySQL HA backends and native High-Availability hooks eliminates lease contention and provides instant failover without lease loss.
* **Nanosecond-Scale Clock Synchronization**: Chrony NTP synchronized against Stratum-1 hardware/PTP or atomic sources prevents Kerberos ticket failures, Raft consensus timeouts, and distributed database corruption.
* **Hardened Operating Posture**: Strict SELinux enforcement, systemd sandboxing (`ProtectSystem=strict`, `NoNewPrivileges=yes`), and minimal network attack surfaces.
""",
        "deliverables": [
            {
                "title": "Authoritative & Recursive BIND 9 DNS with DNSSEC",
                "description": "Primary and secondary BIND 9 DNS servers with split-horizon views, automated inline DNSSEC zone signing, KASP lifecycle rotation, and response-rate limiting (RRL)."
            },
            {
                "title": "High-Availability Kea DHCP Engine",
                "description": "ISC Kea DHCPv4/v6 server deployment with active-active HA hook configuration, PostgreSQL backend for dynamic leases, and TSIG-secured Dynamic DNS (DDNS) integration with BIND9."
            },
            {
                "title": "Precision Chrony NTP Infrastructure",
                "description": "Redundant Chrony NTP servers synchronized against curated Stratum-1 time sources or local GPS/PTP hardware clocks, PPS kernel discipline, and security access control lists."
            },
            {
                "title": "Telemetry, Prometheus Exporters & Disaster Recovery Runbooks",
                "description": "Prometheus exporters for BIND9 and Chrony, structured syslog routing, alerting thresholds for lease exhaustion/clock drift, and comprehensive disaster recovery runbooks."
            }
        ],
        "faqs": [
            {
                "question": "How does Kea DHCP achieve High Availability?",
                "answer": "Kea uses a dedicated C++ HA hook library operating in load-balancing or hot-standby mode. The servers communicate via a secure REST API to synchronize lease state in real time, backed by a clustered PostgreSQL database."
            },
            {
                "question": "Is DNSSEC key rotation automated?",
                "answer": "Yes. We configure BIND 9 Key and Signature Policy (KASP) frameworks that handle automatic ZSK (Zone Signing Key) rollovers and notify administrators when KSK (Key Signing Key) parent DS updates are required."
            }
        ]
    }
]

def main():
    prepared_data = []

    print("=== PREPARING 5 NEW ENTERPRISE SERVICES ===")
    for svc in NEW_SERVICES:
        title = svc["title"]
        print(f"\nPreparing service: {title}...")
        res = contra_cli.call_tool("create_productized_service_prepare", svc)
        sc = res.get("result", {}).get("structuredContent", {})
        if not sc.get("ok"):
            print(f"FAILED: {res}")
            sys.exit(1)
        draft_id = sc.get("draftId")
        summary = sc.get("preview", {}).get("summary", [])
        print(f"  Draft ID: {draft_id}")
        prepared_data.append({
            "title": title,
            "draftId": draft_id,
            "summary": summary
        })

    with open("prepared-5-new-services.json", "w") as f:
        json.dump(prepared_data, f, indent=2)

    print("\nAll 5 new services prepared successfully! Saved to prepared-5-new-services.json.")

if __name__ == "__main__":
    main()
