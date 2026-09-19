==============================================
Sovereign Forgejo & CI/CD Runner Platform Kit
==============================================

:Format: Digital Architecture Blueprint & Automation Kit
:Price: $149.00 USD (One-Time Purchase)
:Target Platform: CentOS Stream 10 / RHEL / Fedora Server
:Core Technologies: Forgejo, Act Runner, Podman Quadlets, PostgreSQL, Caddy, SELinux

Product Overview
================

A production-ready, declarative deployment blueprint for hosting your own ultra-secure Git forge and containerized CI/CD runner fleet on CentOS Stream 10. Eliminate SaaS per-seat license fees ($21–$99/user/month), maintain 100% intellectual property privacy, and run automated pipelines on your own bare-metal or cloud infrastructure.

This complete engineering kit packages rootless Podman Quadlet definitions, PostgreSQL database configurations, automated TLS reverse proxying, and secure runner daemon sandboxes.

What's Included in the Kit
==========================

1. Declarative Podman Quadlet Stack
-----------------------------------

* Native systemd Quadlet files for rootless Forgejo, PostgreSQL, and Caddy.
* Automatic container lifecycle management and auto-updates via ``systemd``.
* Isolated container networks with dedicated bridge interfaces and minimal exposure.

2. Isolated Act Runner Fleet Architecture
-----------------------------------------

* Forgejo Runner (Act Runner) daemon configuration running in rootless Podman mode.
* Hardened build environment sandboxing preventing container breakout or host access.
* Local build artifact and container image caching configurations.
* Sample multi-stage CI/CD workflow templates compatible with GitHub Actions syntax.

3. Hardened Security & Identity Baseline
----------------------------------------

* SELinux Enforcing policy definitions for container storage volumes and unix sockets.
* Automated Caddy reverse proxy configuration with Let's Encrypt TLS and modern ciphers.
* OAuth2 / OIDC and LDAP integration templates for centralized corporate identity.
* Mandatory commit signing verification and branch protection policy templates.

4. Disaster Recovery & Maintenance Automation
---------------------------------------------

* Automated daily snapshot and encrypted backup scripts for PostgreSQL, Git repositories, and LFS objects.
* One-command point-in-time restoration and database disaster recovery scripts.
* Zero-downtime rolling upgrade procedure for Forgejo and PostgreSQL versions.

Post-Purchase Access
====================

Upon purchase, buyers receive instant access to the private repository containing all Quadlet definitions, automation scripts, workflow examples, and a step-by-step administrator guide in RST and Markdown formats.
