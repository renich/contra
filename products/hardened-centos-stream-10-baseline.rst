======================================================
Hardened CentOS Stream 10 & Podman Production Baseline
======================================================

:Format: Digital Architecture Blueprint & Automation Kit
:Price: $195.00 USD (One-Time Purchase)
:Target Platform: CentOS Stream 10 / RHEL 10
:Core Technologies: CentOS Stream 10, Podman, systemd Quadlets, SELinux, firewalld, OpenSCAP

Product Overview
================

A turnkey, production-grade operating system baseline and container runtime architecture designed for mission-critical enterprise workloads. Engineered according to strict EVALinux hardening standards, CIS Linux Benchmarks, and Red Hat Enterprise Linux best practices.

Package your bare-metal servers and cloud instances with automated provisioning, zero-trust network perimeter controls, mandatory SELinux Enforcing posture, and declarative systemd Quadlets.

What's Included in the Baseline
===============================

1. Automated Provisioning & Kickstart Architecture
--------------------------------------------------

* Declarative Anaconda Kickstart profile for automated, unattended CentOS Stream 10 installations.
* Encrypted LVM disk partitioning scheme with dedicated partitions for ``/var``, ``/var/log``, ``/tmp``, and container storage.
* Secure boot and Unified Kernel Image (UKI) compatibility configurations.

2. Defense-in-Depth System Hardening
------------------------------------

* Mandatory SELinux Enforcing configuration with tuned container policies and zero permissive bypasses.
* Hardened Linux kernel sysctl parameters (network stack protection, ASLR, ptrace scope restriction, SYN flood mitigation).
* Restrictive SSH daemon hardening (ed25519 keys only, disabled password auth, root login disabled).
* Declarative ``firewalld`` zone definitions enforcing least-privilege egress and ingress filtering.

3. Rootless Podman & systemd Quadlets Foundation
------------------------------------------------

* Complete systemd Quadlet architecture enabling daemonless, rootless container management.
* Automatic container health checks, journald structured logging, and systemd auto-restart policies.
* Storage volume optimization with overlay2 driver and SELinux volume relabeling (``:z`` / ``:Z``).

4. Automated Compliance & Security Audit Suite
----------------------------------------------

* Automated OpenSCAP compliance scanning scripts validating CIS Benchmark alignment.
* Lightweight system audit scripts for drift detection and unauthorized configuration changes.
* Comprehensive hardening checklist and production readiness verification runbook.

Post-Purchase Access
====================

Upon purchase, buyers receive immediate access to the private repository containing all Kickstart profiles, Ansible roles, Quadlet templates, sysctl configs, and operational runbooks.
