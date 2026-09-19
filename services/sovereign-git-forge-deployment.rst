=========================================================
Sovereign Git Forge & CI/CD Runner Platform Deployment
=========================================================

:Format: Fixed-Scope Engineering Sprint
:Price: $4,000 USD (Fixed Price)
:Timeline: 1–2 weeks
:Target Platform: CentOS Stream 10 / Red Hat Enterprise Linux / Fedora Server
:Core Technologies: Forgejo, Forgejo Runner (Act Runner), Podman Quadlets, PostgreSQL, Caddy, SELinux

Executive Overview
==================

Eliminate escalating per-seat SaaS costs ($21–$99/user/month on GitHub Enterprise or GitLab SaaS), protect proprietary intellectual property from third-party AI training ingestion, and achieve total source code sovereignty.

We design, deploy, and harden a turnkey, self-hosted Git platform powered by **Forgejo** and containerized **CI/CD build runners** running on **CentOS Stream 10**. The resulting environment provides a frictionless GitHub/GitLab-compatible developer experience with enterprise-grade isolation, automated pipeline execution, and zero recurring software licensing fees.

Why Sovereign Git Infrastructure?
=================================

* **Zero Per-Seat SaaS Tax**: Host unlimited developers, repositories, and CI/CD pipelines on your own bare-metal or cloud infrastructure without recurring license charges.
* **Total Intellectual Property Privacy**: Keep proprietary algorithms, source code, and secrets strictly within your private network boundaries, completely air-gapped from commercial AI scraping.
* **Lightweight & High-Performance**: Forgejo's compiled Go engine uses a fraction of the memory and compute overhead required by monolithic GitLab or Java-based alternatives.
* **Hardened Security Posture**: Production deployment hardened with strict SELinux Enforcing policies, rootless Podman container execution, and automated TLS lifecycle management.

Core Deliverables
=================

1. Production Forgejo Deployment on CentOS Stream 10
----------------------------------------------------

* Dedicated Forgejo platform deployed using declarative systemd Quadlets and rootless Podman containers.
* Production-tuned PostgreSQL database backend with automated connection pooling and WAL archiving.
* Automated TLS certificate issuance and renewal via reverse proxy (Caddy or Nginx) with modern cipher suites and HTTP/3 support.
* Git Large File Storage (Git LFS) configuration backed by local high-speed NVMe or S3-compatible object storage.

2. Dedicated CI/CD Runner Fleet (Act Runner)
--------------------------------------------

* Automated build runner daemon (Forgejo Runner) supporting standard GitHub Actions workflow syntax (``.forgejo/workflows`` or ``.github/workflows``).
* Isolated rootless container execution environments preventing workflow privilege escalation or host contamination.
* Intelligent local build dependency caching to minimize network egress and slash pipeline build times.
* Dedicated worker auto-cleanup and resource quotas (CPU, memory, storage bounds).

3. Zero-Trust Security & Identity Integration
---------------------------------------------

* Integration with corporate identity providers (OAuth2, OpenID Connect, LDAP/Active Directory, or SAML).
* Strict branch protection rules, mandatory code review gates, and automated commit signature (GPG/SSH) enforcement.
* Role-Based Access Control (RBAC) configured for teams, organizations, and external contractors.
* Hardened firewall rules (firewalld) and mandatory SELinux Enforcing posture across host and container volumes.

4. Backup Automation & Disaster Recovery Runbook
------------------------------------------------

* Automated daily snapshot and backup pipeline coordinating PostgreSQL dumps, Git repository data, and LFS objects.
* Encrypted off-site backup synchronization with retention lifecycle policies.
* Tested point-in-time recovery procedure with step-by-step restoration verification.
* Comprehensive administration runbook and operational training session for internal platform maintainers.

Engagement Process
==================

#. **Phase 1: Architecture & Requirements Intake (Day 1–2)**:
   Review existing version control setup (GitHub, GitLab, Bitbucket, or legacy Git), user directory requirements, and CI/CD pipeline dependencies.

#. **Phase 2: Platform Deployment & Hardening (Day 3–5)**:
   Provision CentOS Stream 10 host, configure rootless Podman Quadlets, initialize PostgreSQL, deploy Forgejo, and apply SELinux policies.

#. **Phase 3: CI/CD Runner Cluster Setup (Day 6–8)**:
   Deploy Act Runner daemon, build specialized build container images, and validate test workflows.

#. **Phase 4: Migration & Integration Pilot (Day 9–10)**:
   Import pilot repositories, configure SSO/LDAP integration, and verify commit signing and branch protection.

#. **Phase 5: Operational Handover & Runbook Delivery (Day 11–12)**:
   Deliver administrative documentation, verify automated backup snapshots, and conduct technical handover with your engineering team.
