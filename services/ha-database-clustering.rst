=========================================================
High-Availability Database Cluster Deployment & Hardening
=========================================================

:Format: Fixed-Scope Engineering Sprint
:Price: $5,000 USD (Fixed Price)
:Timeline: 2 weeks
:Target Platform: CentOS Stream 10 / RHEL 10 / PostgreSQL / MariaDB Galera
:Core Technologies: PostgreSQL (Patroni, pgBouncer, WAL-G), MariaDB Galera, Keepalived/HAProxy, SELinux

Executive Overview
==================

Eliminate database single points of failure, prevent costly application outages during hardware failures or maintenance windows, and ensure verifiable zero data loss.

We architect, deploy, and benchmark high-availability database clusters powered by **PostgreSQL** (with **Patroni**, **pgBouncer**, and **WAL-G**) or **MariaDB Galera** synchronous multi-master clusters on hardened **CentOS Stream 10**. Every deployment includes sub-second automated failover, connection pooling, continuous streaming backups, and verified point-in-time recovery (PITR).

Why Professional HA Database Clustering?
========================================

* **Zero-Downtime Maintenance**: Perform operating system upgrades, security patches, and hardware replacements on individual nodes without taking your application offline.
* **Sub-Second Automated Failover**: Distributed consensus agents detect node or network failures and promote healthy replicas instantaneously without manual intervention.
* **Connection Pooling & Query Routing**: Decouple application connection spikes from backend database worker limits using high-performance connection pooling.
* **Verifiable Disaster Recovery**: Continuous transaction log streaming to S3-compatible object storage with automated point-in-time recovery drills.

Core Deliverables
=================

1. Multi-Node Synchronous Database Cluster
------------------------------------------

* Multi-node cluster deployment (PostgreSQL with Patroni/etcd consensus or MariaDB Galera multi-master).
* Automated master/replica promotion and quorum management preventing split-brain scenarios.
* Dedicated private network synchronization with optimized network MTU and sysctl TCP buffer tuning.

2. Connection Pooling & Intelligent Load Balancing
--------------------------------------------------

* Dedicated connection pooling layer (pgBouncer or HAProxy) configured with transaction-level pooling.
* Read/write query splitting routing write traffic to primary nodes and read queries across healthy read replicas.
* Health-check probes with sub-second backend isolation during maintenance or degraded states.

3. Continuous Streaming Backups & Point-in-Time Recovery
--------------------------------------------------------

* Continuous WAL archiving (WAL-G or pgBackRest) streaming encrypted transaction logs to S3-compatible storage.
* Automated daily base backup snapshots with configurable retention and grandfather-father-son (GFS) rotation.
* Documented point-in-time recovery (PITR) drill verifying restoration to a specific minute or transaction ID.

4. Kernel & Storage Performance Hardening
-----------------------------------------

* Linux kernel sysctl optimization (dirty memory ratios, hugepages, overcommit parameters, and shared memory limits).
* Storage I/O scheduling and filesystem tuning (XFS/ext4 mount options, WAL disk separation).
* Mandatory SELinux Enforcing posture confining database processes, sockets, and storage volumes.

Engagement Process
==================

#. **Phase 1: Architecture & Workload Intake (Day 1–2)**:
   Analyze transaction rates, schema sizes, query profiles, read/write ratios, and recovery time objectives (RTO/RPO).

#. **Phase 2: Cluster Provisioning & OS Hardening (Day 3–5)**:
   Deploy CentOS Stream 10 nodes, configure private networking, apply kernel sysctls, and enforce SELinux policies.

#. **Phase 3: Database Engine & Consensus Deployment (Day 6–8)**:
   Initialize database engine, configure synchronous replication, set up Patroni/Galera quorum, and test consensus failure modes.

#. **Phase 4: Connection Pooling & Disaster Recovery Drill (Day 9–11)**:
   Deploy pgBouncer/HAProxy, configure continuous WAL archiving to S3, and execute an end-to-end PITR restoration drill.

#. **Phase 5: Benchmarking, Runbooks & Handover (Day 12–14)**:
   Execute pgbench/sysbench stress tests, deliver operational runbooks, and conduct administrative training with your engineering team.
