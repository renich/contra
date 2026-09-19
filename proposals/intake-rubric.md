# Client Intake & Lead Triage Rubric

Use this checklist to evaluate inbound Contra inquiries, job briefs, or direct messages in under 5 minutes.

---

## 1. Technical Fit Gate (Pass/Fail)

- [ ] **Infrastructure / Systems Alignment**:
  - Linux (Fedora, RHEL, Debian/Ubuntu)
  - Containers / Orchestration (Podman, Docker, systemd Quadlets, Nomad/Kubernetes)
  - CI/CD & Automation (GitLab CI, GitHub Actions, Ansible, Make)
  - Systems Programming / Tooling (Crystal, Go, Bash, C/C++, Python)
  - Security & Hardening (SELinux, PKI/TLS, zero-trust, air-gapped systems)
  - AI & Agent Engineering (LLM workflow integration, local agent tooling, autonomous systems)
- [ ] **Anti-Fit Trigger (Instant Reject)**:
  - Frontend-only React/Next.js/Vue component assembly.
  - Windows Server/Active Directory administration.
  - Undocumented legacy proprietary blobs with zero test suites.
  - Unclear "build me an entire SaaS from scratch for $500".

---

## 2. Commercial Viability Gate

- [ ] **Budget Realism**:
  - Fixed-price milestone corresponds to minimum rate ($1,000+ per milestone / project).
  - Retainers start at $1,500+/week or $5,000+/month.
  - Client accepts milestone-based escrow on Contra.
- [ ] **Timeline Realism**:
  - No emergency fire drills without an explicit emergency surge surcharge (+50% to +100%).
  - Clear milestone horizons (1–2 weeks per deliverable).

---

## 3. Communication & Governance Gate

- [ ] **Async Tolerance**:
  - Client respects async-first workflow (written briefs, PRs, weekly digests).
  - No demand for daily standups or surveillance time-tracking apps.
- [ ] **Decision Maker Access**:
  - Direct line of communication to CTO, VP of Eng, or Founder.
  - Not filtered through 3 layers of non-technical project managers.

---

## Decision Matrix

| Score | Recommendation | Action |
|---|---|---|
| **3/3 Gates Pass** | **Strong Fit** | Schedule 20-min architecture discovery call or send bespoke async scoping questions. |
| **Technical Pass, Low Budget** | **Scope Compression** | Offer reduced-scope fixed audit or template-based consulting. |
| **Failed Technical or Governance** | **Polite Decline** | Send fast decline template within 2 hours. Protect time ruthlessly. |
