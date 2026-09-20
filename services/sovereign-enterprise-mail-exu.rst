=======================================================
Sovereign Enterprise Mail Server & exu Suite Deployment
=======================================================

:Format: Fixed-Scope Engineering Sprint
:Price: $3,000 USD (Fixed Price)
:Timeline: 1 week
:Target Platform: CentOS Stream 10 / Exim / Dovecot / Caddy / exu Suite
:Core Technologies: exu Suite (Crystal), Exim MTA, Dovecot IMAP/POP3, Caddy, mutual TLS (mTLS), DKIM/DMARC/SPF

Executive Overview
==================

Escape recurring per-user SaaS license fees ($6–$30/user/month on Microsoft 365 or Google Workspace), retain absolute data sovereignty over executive correspondence, and eliminate email deliverability failures.

We deploy and harden a sovereign, high-deliverability enterprise mail infrastructure powered by **EVALinux exu Suite**, **Exim**, **Dovecot**, and **Caddy** on **CentOS Stream 10**. Built with a statically compiled Crystal daemon and CLI, ``exu`` provides an intuitive Single-Page Application (SPA) web control plane protected by client-certificate mTLS authentication, alongside native command-line administration (`eum`), automated 2048-bit DKIM key generation, and copy-paste ready DNS records for a guaranteed **10/10 deliverability score**.

Why Sovereign Enterprise Mail with exu?
=======================================

* **Zero Per-Seat SaaS Taxes**: Host unlimited domains, mailboxes, and aliases on your private server infrastructure without recurring per-inbox fees.
* **100% Data Privacy & Legal Sovereignty**: Retain full ownership of corporate email archives, protected from automated cloud scanning and foreign legal jurisdiction.
* **Guaranteed 10/10 Deliverability**: Perfect inbox placement backed by automated RSA-2048 DKIM signing, strict SPF alignment, DMARC enforcement, and verified rDNS/PTR configuration.
* **Bank-Grade Security**: Decoupled transport mTLS client certificate authentication with encrypted HMAC-SHA256 session cookies, POSIX advisory locking, and non-invasive modular MTA configuration files.

Core Deliverables
=================

1. Turnkey exu Virtual Mail Suite Deployment
--------------------------------------------

* Production installation of statically-compiled ``exu`` daemon, ``eum`` CLI utility, Exim MTA, and Dovecot IMAP/POP3 on CentOS Stream 10.
* Standardized FHS 3.0 configuration hierarchy in ``/etc/exu/`` with human-readable YAML 1.2 database.
* Modular Exim includes and Dovecot configuration drop-ins preventing package update conflicts (zero ``.rpmnew`` churn).

2. Web Control Dashboard & mTLS Authentication
----------------------------------------------

* Modern, responsive Single-Page Application (SPA) web interface for domain, user, and alias administration.
* Enterprise mutual TLS (mTLS) client certificate verification enforcing hardware-backed or browser-installed certificate login.
* Automated client certificate generation and management playbooks for administrative staff.

3. Complete Deliverability & Cryptographic DNS Baseline
-------------------------------------------------------

* Automated generation and rotation of RSA-2048 DKIM cryptographic keys per virtual domain.
* Complete, verified DNS record templates ready for copy-pasting (MX, SPF, DKIM public keys, and strict DMARC policies).
* Validation of reverse DNS (PTR) records, TLS cipher suites, and verification of a **10/10 mail-tester deliverability score**.

4. Virtual Domains, Multi-Recipient Aliases & Autodiscover
----------------------------------------------------------

* Multi-domain hosting with configurable default alias templates automatically seeded upon domain creation.
* Robust multi-recipient alias forwarding supporting space-, comma-, or semicolon-delimited recipient lists.
* Native client auto-configuration endpoints for Mozilla Thunderbird and Microsoft Outlook autodiscover protocols.
* Automated daily mailbox backup and snapshot scripts with configurable retention policies.

Engagement Process
==================

#. **Phase 1: Domain & Host Architecture Intake (Day 1)**:
   Verify server reverse DNS (PTR), clean IP reputation, DNS hosting provider, and target domain inventory.

#. **Phase 2: Platform Provisioning & MTA Hardening (Day 2–3)**:
   Deploy CentOS Stream 10 host, configure Exim, Dovecot, and Caddy with Let's Encrypt TLS certificates, and install ``exu`` daemon.

#. **Phase 3: mTLS PKI & Web Control Plane Setup (Day 4)**:
   Generate administrative client certificates, configure Caddy client authentication, and initialize ``exu`` web control plane.

#. **Phase 4: Deliverability Verification & Testing (Day 5)**:
   Configure virtual domains, generate DKIM keypairs, apply DNS records, and execute deliverability test suites across major inboxes.

#. **Phase 5: Operational Delivery & Runbook Handover (Day 6–7)**:
   Deliver administrator runbooks, review CLI (`eum`) management workflows, verify automated backups, and conduct technical handover.
