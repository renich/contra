======================================================================
Core Sovereign Network Services: BIND9 DNSSEC, Kea DHCP & Chrony NTP
======================================================================

:Format: Fixed-Scope Engineering Sprint
:Price: $3,500 USD (Fixed Price)
:Timeline: 1 week
:Target Platform: Fedora / CentOS Stream 10 / RHEL 9/10 / Linux Containers
:Core Technologies: BIND 9.18+, DNSSEC, Kea DHCP (HA Hook & PostgreSQL backend), Chrony NTP, Firewalld, SELinux

Executive Overview
==================

Flawed DNS resolution, fragile DHCP single points of failure, and unsynchronized system clocks cascade into catastrophic outages, broken TLS handshakes, distributed database split-brains, and invalid audit logs.

We engineer sovereign, enterprise-grade core network infrastructure built on the gold standards of Internet engineering: authoritative and recursive **BIND 9** with automated **DNSSEC** signing, high-throughput **Kea DHCP** with active-active High-Availability database clustering, and sub-millisecond precision **Chrony NTP** time synchronization. This triad provides the rock-solid, resilient foundation required for modern datacenter, campus, and hybrid cloud operations.

Why Sovereign Core Network Infrastructure?
==========================================

* **Cryptographic DNS Integrity**: BIND9 with automated DNSSEC key management (inline signing, KASP policies) protects internal and public zones against DNS cache poisoning, spoofing, and man-in-the-middle exploits.
* **Resilient Active-Active DHCP**: Kea DHCP with PostgreSQL/MySQL HA backends and native High-Availability hooks eliminates lease contention and provides instant failover without lease loss.
* **Nanosecond-Scale Clock Synchronization**: Chrony NTP synchronized against Stratum-1 hardware/PTP or atomic sources prevents Kerberos ticket failures, Raft consensus timeouts, and distributed database corruption.
* **Hardened Operating Posture**: Strict SELinux enforcement, systemd sandboxing (``ProtectSystem=strict``, ``NoNewPrivileges=yes``), and minimal network attack surfaces.

Core Deliverables
=================

1. Authoritative & Recursive BIND 9 DNS with DNSSEC
---------------------------------------------------

* Deployment of primary and secondary BIND 9 DNS servers with split-horizon view configurations separating internal RFC 1918 traffic from external clients.
* Automated DNSSEC key generation, inline zone signing, and automated Key and Signature Policy (KASP) lifecycle rotation.
* High-performance response-rate limiting (RRL) mitigating DNS amplification attacks, alongside recursive caching with DNS over TLS (DoT) upstream encryption.

2. High-Availability Kea DHCP Engine
------------------------------------

* Modern ISC Kea DHCPv4 and DHCPv6 server deployment with high-performance C++ core architecture.
* Active-active or hot-standby High-Availability hook configuration with sub-second lease database synchronization.
* Scalable PostgreSQL backend storage for dynamic lease allocations, host reservations, and subnet option templates.
* Dynamic DNS (DDNS) integration securely pushing forward and reverse PTR records directly to BIND9 using TSIG transaction keys.

3. Precision Chrony NTP Infrastructure
--------------------------------------

* Redundant Chrony NTP server deployment configured with curated public Stratum-1 time sources or local GPS/PTP hardware clocks.
* Kernel-level PPS (Pulse Per Second) discipline and hardware timestamping configuration achieving microsecond-to-nanosecond accuracy.
* Access control lists (ACLs) restricting NTP queries, frequency drift tracking, and leap-second handling policies.

4. Monitoring, Audit & Operational Runbooks
-------------------------------------------

* Prometheus exporters for BIND9 (bind_exporter) and Chrony (chrony_exporter) tracking query volumes, cache hit ratios, lease exhaustion rates, and clock offset metrics.
* Structured logging integration routing lease transitions and DNS audit events to centralized log analytics.
* Comprehensive disaster recovery runbooks covering zone reconstitution, manual DNSSEC key rollovers, and database recovery.

Engagement Process
==================

Day 1: Subnet Mapping, Zone Audit & Topology Blueprint
   Audit IP address plans, domain hierarchies, VLAN boundaries, and NTP synchronization upstream sources.

Days 2–3: BIND9 DNSSEC & Kea DHCP HA Cluster Deployment
   Deploy primary/secondary DNS, configure inline DNSSEC, set up Kea DHCP engine with PostgreSQL backend, and wire TSIG DDNS updates.

Day 4: Chrony Precision Time Synchronization & Security Hardening
   Deploy Chrony servers, calibrate clock drift, enforce systemd sandboxing, and configure firewalld rules.

Day 5: Failover Chaos Testing, Telemetry Dashboards & Handover
   Simulate primary node crashes, verify instantaneous DHCP/DNS failover, inspect Prometheus metrics, and deliver operational documentation.
