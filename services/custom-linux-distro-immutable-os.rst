===================================================================
Custom Linux Distribution & Immutable OS Engineering: mkosi & UKI
===================================================================

:Format: Fixed-Scope Engineering Sprint
:Price: $6,000 USD (Fixed Price)
:Timeline: 2 weeks
:Target Platform: CentOS Stream 10 / Fedora / RHEL / Bare Metal / Cloud / Edge
:Core Technologies: mkosi, Unified Kernel Images (UKI), systemd-repart, systemd-boot, dm-verity, TPM2, SecureBoot, systemd-sysext

Executive Overview
==================

Traditional mutable operating systems suffer from configuration drift, silent package corruption, unauthorized tampering, and slow, non-deterministic recovery workflows.

We architect and build tailored, reproducible, and cryptographically verified Linux operating system distributions and appliances from source or upstream RPM repositories. Powered by modern **mkosi**, **Unified Kernel Images (UKIs)**, **systemd-repart**, and **dm-verity**, our immutable operating system images boot directly into read-only, cryptographically authenticated environments with hardware-backed TPM2 Secure Boot sealing, guaranteeing total platform integrity from bare-metal firmware to application runtimes.

Why Custom Immutable Linux Distributions?
=========================================

* **Zero Configuration Drift**: The root filesystem is strictly read-only and sealed with dm-verity hashes, ensuring that every deployment across edge, virtualization, or bare-metal is mathematically identical.
* **Tamper-Proof Boot Chain**: Unified Kernel Images (combining Linux kernel, initrd, and kernel cmdline into a single PE binary) signed with private SecureBoot keys and sealed to TPM2 PCR registers.
* **Atomic A/B Upgrades**: Dual-bank partition layouts orchestrated by ``systemd-sysupdate`` and ``systemd-repart`` provide instantaneous, fail-safe updates with automated fallback upon boot failure.
* **Modular System Extensions**: Granular customization and zero-reboot runtime extension delivery via signed ``systemd-sysext`` and ``systemd-confext`` images.

Core Deliverables
=================

1. Declarative mkosi Build Pipeline
-----------------------------------

* Comprehensive, version-controlled ``mkosi`` recipes defining distribution packages, kernel parameters, filesystem hierarchies, and user accounts.
* Fully reproducible build pipelines generating raw disk images, QCOW2 virtual machine appliances, and ISO live boot media.
* Clean separation of OS root filesystems from persistent state partitions (``/var``, ``/etc`` overlay).

2. Unified Kernel Image (UKI) Architecture
------------------------------------------

* Synthesis of kernel, systemd-stub, OS release credentials, initrd, and boot command-line into a single Unified Kernel Image binary.
* Generation and enrollment of private SecureBoot keys (PK, KEK, db) and automated image signing pipelines.
* Integration of TPM2 measurement and PCR sealing binding decryption keys directly to verified platform boot states.

3. Immutable dm-verity Root & Partition Engineering
---------------------------------------------------

* Declarative partition schemes authored with ``systemd-repart`` supporting automatic disk growth, GPT partition UUID standards, and LUKS2 disk encryption.
* Cryptographic root integrity verification using ``dm-verity`` trees embedded directly into UKI binaries or signed roothash descriptors.
* Resilient read-only mount policies with ephemeral tmpfs overlays for ephemeral application runtime workspaces.

4. Extension Management & Update Orchestration
----------------------------------------------

* Authoring of ``systemd-sysext`` overlay packages allowing modular application updates without touching the base operating system image.
* Setup of native OS update server infrastructure utilizing ``systemd-sysupdate`` for atomic, bandwidth-efficient differential deployments.
* Complete deployment runbooks, testing fixtures in QEMU/KVM, and automated CI/CD image build workflows.

Engagement Process
==================

Week 1: Requirements Intake, Package Scoping & mkosi Baseline
   Define required packages, kernel requirements, hardware targets, and create the baseline declarative build manifest.

Week 2: UKI Signing, dm-verity Sealing & Automated Pipeline Handover
   Integrate SecureBoot signing, configure TPM2/dm-verity security controls, validate A/B upgrade mechanics in KVM, and deliver build pipelines.
