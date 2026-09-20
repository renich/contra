===================================================================
Enterprise FreeIPA HA & Centralized PKI/CA Infrastructure
===================================================================

:Format: Fixed-Scope Engineering Sprint
:Price: $5,500 USD (Fixed Price)
:Timeline: 2 weeks
:Target Platform: Red Hat Enterprise Linux / CentOS Stream 9/10 / Fedora
:Core Technologies: FreeIPA / Red Hat IdM, 389 Directory Server, MIT Kerberos, Dogtag Certificate System, SSSD, Certmonger, DNSSEC, Ansible IdM

Executive Overview
==================

Fragmented user accounts, scattered SSH keys, unmanaged sudo privileges, and expired TLS certificates represent the largest operational security liabilities in modern infrastructure.

We deploy a production-hardened, multi-master High-Availability (HA) FreeIPA / Red Hat Identity Management (IdM) domain combined with a multi-tier Public Key Infrastructure (PKI). This unified sovereign architecture delivers centralized identity management, Kerberos Single Sign-On (SSO), Host-Based Access Control (HBAC), automated host certificate issuance, and centralized sudo governance across your entire Linux server fleet.

Why Enterprise FreeIPA & Centralized Identity?
==============================================

* **Zero Identity Fragmentation**: Single authoritative directory for user credentials, SSH public keys, groups, and netgroups across all hybrid cloud and bare-metal nodes.
* **Granular Host & Command Governance**: Fine-grained Host-Based Access Control (HBAC) and centralized sudo rule evaluation enforced natively by System Security Services Daemon (SSSD).
* **Multi-Master Replication & Zero Downtime**: Active-active directory topologies with multi-master LDAP and Kerberos replication, automated conflict resolution, and integrated DNS round-robin failover.
* **Automated Certificate Lifecycle**: Integrated Dogtag Certificate System with automated host/service TLS certificate enrollment and renewal via ``certmonger`` and ACME endpoints.

Core Deliverables
=================

1. Multi-Master High-Availability FreeIPA Domain
------------------------------------------------

* Architecture and deployment of a minimum 2-node or 3-node HA FreeIPA topology with multi-master replication across separate availability zones or datacenters.
* Automated directory synchronization covering LDAP databases, Kerberos key distribution centers (KDC), and integrated DNS zones.
* Hardened firewall policies, TLS 1.3 encrypted directory transport (LDAPS/STARTTLS), and automated disaster recovery backup playbooks.

2. Centralized PKI Architecture & Sub-CA Management
---------------------------------------------------

* Full deployment and configuration of Dogtag Certificate System integrated natively into FreeIPA.
* Hierarchical Certificate Authority design supporting an offline/external enterprise Root CA with subordinate FreeIPA Issuing CAs, or a standalone self-hosted trust anchor.
* Custom certificate profiles, automated certificate revocation list (CRL) publication, and Online Certificate Status Protocol (OCSP) responders.

3. Automated Host Enrollment & SSSD Hardening
---------------------------------------------

* Automated, idempotent client enrollment playbooks utilizing the official Ansible ``ansible.posix`` and ``freeipa.ansible_freeipa`` collections.
* Hardened SSSD client configuration with offline credential caching, Kerberos ticket renewal daemons, and failover domain priority.
* Automated deployment of ``certmonger`` for zero-touch host and service certificate tracking, automated renewal, and post-renewal daemon reloads.

4. Role-Based Access Control, HBAC & Centralized Sudo
-----------------------------------------------------

* Hierarchical user group hierarchy, administrative roles, and least-privilege RBAC delegation.
* Implementation of strict Host-Based Access Control (HBAC) policies governing which teams and users can access specific production tiers.
* Centralized sudo command catalogs and rule definitions eliminating unmanaged ``/etc/sudoers`` drift across cluster nodes.

Engagement Process
==================

Week 1: Topology Design, DNS Integration & Master Domain Deployment
   Finalize realm topology, configure DNS forward/reverse resolution, deploy primary FreeIPA master, and validate integrated PKI subsystems.

Week 2: Replica Provisioning, Client Automation & Handover
   Deploy and synchronize HA replica nodes, implement Ansible client enrollment pipelines, configure HBAC/sudo governance, and conduct failover simulation tests.
