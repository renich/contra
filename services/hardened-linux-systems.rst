==================================================
Service: Hardened Linux & Container Infrastructure
==================================================

:Pricing Model: Fixed Scope / Milestone-based ($3,500 – $8,000)
:Turnaround: 2 to 3 weeks
:Delivery Vehicle: Infrastructure-as-Code (Ansible/systemd Quadlets), SELinux Policies, Verification Test Suite

What This Solves
================

Standard Linux cloud instances and default container setups run with dangerous privileges: root daemons, broad attack surfaces, permissive SELinux, unauthenticated local sockets, and vulnerable supply chains.

This service transforms your Linux hosts and container environments into hardened, immutable, zero-trust infrastructure designed to withstand hostile environments and strict compliance audits.

Scope & Implementation Modules
==============================

SELinux & Kernel Hardening
--------------------------

* Transition systems to SELinux **Enforcing** mode without breaking production workloads.
* Author custom Type Enforcement (``.te``) policies for bespoke applications.
* Kernel sysctl tuning for network security, memory protection, and resource containment.

Rootless Containers & Systemd Quadlets
--------------------------------------

* Migrate privileged Docker daemons to rootless Podman managed natively by systemd Quadlets.
* User namespace mapping, secure volume labeling (``:z``/``:Z``), and unprivileged socket isolation.

PKI, TLS & Secret Hygiene
-------------------------

* End-to-end TLS configuration, private certificate authority (CA) setup, and automated renewal.
* Secure filesystem permissions (``600`` for keys), memory-backed tmpfs for runtime secrets, and zero-plaintext storage.

Reproducible OS Images & RPM Packaging
--------------------------------------

* Declarative system image generation (mkosi, Unified Kernel Images / UKIs).
* Custom RPM packaging for internal binaries following strict Fedora/EPEL packaging standards.

Deliverables
============

* Fully automated Ansible playbooks (FQCN standard) or systemd Quadlet manifests.
* Documented rollback procedures and SELinux troubleshooting runbooks.
* Automated compliance and security audit test suite verifying the hardened posture.
