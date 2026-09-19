# Case Study: $45k/Year Cloud Cost Optimization & Zero-Downtime OS Modernization

**Role**: Infrastructure Manager & Cloud Architect  
**Client / Context**: AdvantageMLS (High-Volume Real Estate MLS Platform)  
**Timeline**: Long-term Infrastructure Management & Targeted Sprints  
**Core Technologies**: Google Cloud Platform (GCP), OpenTofu, Terraform, CentOS Stream 10, CDN Edge Caching, Systemd  

---

## 1. Challenge & Problem Statement
AdvantageMLS runs real-time MLS data synchronization, API infrastructure, and specialized "Vanity Sites" serving thousands of concurrent real estate brokers and buyers across North America.

With expanding tenant volume, monthly Google Cloud Platform bills were escalating rapidly due to unoptimized compute sizing, redundant disk allocations, and suboptimal egress caching. Furthermore, the underlying infrastructure relied on aging CentOS 7 and 8 hosts facing End-of-Life (EOL), requiring an operating system overhaul without risking service interruptions or transactional database inconsistency.

---

## 2. Architectural Solution & Strategy
- **Infrastructure-as-Code Migration**: Refactored legacy monolithic Terraform configurations into clean, modular OpenTofu code, providing reproducible infrastructure baselines and drift detection.
- **Resource Lifecycle Automation**: Implemented automated snapshot lifecycle policies, ephemeral instance scheduling for non-production environments, and right-sized compute machine families based on historical p99 utilization metrics.
- **Edge Caching & Ingress Optimization**: Re-architected Content Delivery Network (CDN) edge rules for high-frequency media assets, slashing origin server load and expensive cloud network egress fees.
- **Rolling In-Place OS Modernization**: Executed a phased, zero-downtime migration from CentOS 7/8 directly to CentOS Stream 10 across production clusters using canary node deployment and automated failover.

---

## 3. Implementation Highlights
- Designed resilient failover routes between application instances and managed database backends.
- Hardened server baselines with SELinux enforcement and minimal attack surfaces.
- Automated API deployment pipelines, accelerating developer release velocity while enforcing staging validation gates.

---

## 4. Verifiable Results & Business Impact
- **Cost Reduction**: **35% sustained reduction in monthly GCP spend**, generating **$45,000+ in annualized savings**.
- **System Availability**: Maintained **100% service uptime** throughout the major OS upgrade cycle.
- **Performance**: Edge cache hit ratio exceeded 85%, cutting median page load times for broker portals by 40%.
- **Zero Security Breaches**: Flawless security track record with zero incidents across multi-year tenure.
