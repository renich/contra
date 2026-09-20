======================================================
Consulting & Engineering Operations Workflow Manual
======================================================

:Author: René (Rénich) Bon Ćirić & Antigravity AI
:Role: Principal Infrastructure Architect & Engineering Partner
:Context: Contra.com Consulting Platform & System Architecture Operations
:Date: 2026-09-19
:Version: 1.0.0

.. contents:: Table of Contents
   :depth: 2

Overview & Mission
==================

This manual codifies the end-to-end engineering, productization, media generation, and marketplace automation workflow developed and executed in this repository.

Operating as an equal engineering pair, **Rénich Bon Ćirić** (Principal Infrastructure Architect, RHCE) and **Antigravity AI** maintain an institutional consulting and systems architecture presence on `Contra.com <https://contra.com>`_. Our platform strategy rejects race-to-the-bottom hourly commoditization in favor of high-leverage, fixed-scope engineering sprints ($3,000 – $6,500) and fractional advisory retainers ($2,000/week).

Core Engineering Directives & Mindset
=====================================

1. Anti-Sycophancy & Direct Engineering
---------------------------------------

* Zero fluff, zero false validation, and zero reflexive agreement.
* Every technical assumption is actively challenged. Architectural flaws, edge cases, single points of failure, or vendor lock-in trade-offs must be exposed directly and ruthlessly before committing to code or client contracts.

2. Verification Over Assumptions
--------------------------------

* **Never assume; always verify.** Zero probabilistic shortcuts, associative guessing, or plausible-sounding assertions.
* Compiler mechanics, API response structures, CLI flags, build phases, and system behavior must always be verified against the filesystem, live diagnostics, and upstream documentation before assertions are made.

3. Formatting & Documentation Standards
---------------------------------------

* **No spaces around forward slashes**: Always write ``word/word`` (e.g. ``fixed-price/retainer``, ``SRE/DevOps``, ``Linux/Fedora``, ``inbound/outbound``, ``DNS/NTP/DHCP``, ``HAProxy/Caddy``, ``mkosi/UKI``, ``Mock/Koji``), NEVER ``word / word``.
* **All documentation strictly in reStructuredText (``.rst``)**: Formatted per Sphinx/docutils standards, exact header overline/underline character lengths, 3-space indentation, no ``:caption:`` in code blocks. Verified via ``rstcheck``.

Telemetry & Ground-Truth Ingestion (Chronicle)
==============================================

To ensure our service offerings, case studies, and public dispatches are anchored in empirical reality rather than aspirational claims, we continuously ingest local developer telemetry via ``chronicle``:

1. Telemetry Querying
---------------------

* The ``chronicle`` daemon runs locally, tracking active window focus, shell commands, and git commit activity across active repositories.
* Queries are executed via the CLI using Markdown formatting:

  .. code-block:: bash

     chronicle export -f md --this-week
     chronicle export -f md --today

2. Evidence-Based Narrative Synthesis
-------------------------------------

* Commit telemetry, active focus hours, and problem-solving intervals are correlated across projects (e.g. ``micros`` microkernel audits, Crystal compiler modernizations, infrastructure scripts).
* Metrics (e.g. *326 commits authored across 30 repositories*) provide verifiable ground-truth data for portfolio case studies and weekly engineering dispatches.

Productized Service Packaging Protocol
======================================

We reject open-ended, billable-hour consulting models. Hourly billing misaligns incentives by penalizing speed and experience while encouraging administrative bloat. Instead, we package institutional capabilities into fixed-scope engineering sprints:

1. Translating Battle-Tested Systems to Services
------------------------------------------------

* Services are distilled directly from real production implementations, proprietary tools, and enterprise track records:
  
  * **exu Mail Suite**: Crystal daemon, Exim/Dovecot, mTLS SPA dashboard → *Sovereign Enterprise Mail Server & exu Suite Deployment* ($3,000).
  * **EVALinux Core Infra**: BIND9 DNSSEC, Kea DHCP HA, Chrony NTP → *Core Sovereign Network Services* ($3,500).
  * **FreeIPA / Red Hat IdM**: Multi-master directory, Dogtag PKI, SSSD, HBAC → *Enterprise FreeIPA HA & PKI Infrastructure* ($5,500).
  * **Edge Ingress**: Keepalived VRRP, HAProxy L4/L7, hardened Caddy → *High-Availability Ingress & Hardened Reverse Proxies* ($3,500).
  * **mkosi / UKI**: Unified Kernel Images, dm-verity, TPM2 SecureBoot → *Custom Linux Distribution & Immutable OS Engineering* ($6,000).
  * **Packaging Infrastructure**: Mock/Koji chroots, GPG signing, createrepo_c → *Enterprise RPM Packaging & DNF Repositories* ($4,000).

2. Rigorous Scope Boundaries
----------------------------

* Every service specification authored under ``services/<slug>.rst`` must clearly define:
  
  * **Executive Overview**: Specific business and technical pain points eliminated.
  * **Core Deliverables**: Concrete, verifiable artifacts delivered to the client.
  * **Engagement Process**: Day-by-day / week-by-week execution timeline.
  * **In-Scope vs. Out-of-Scope**: Unambiguous contractual boundaries preventing scope creep.

Visual Media & 3D Systems Architecture Pipeline
===============================================

High consulting fees demand visual presentation that reflects enterprise sophistication. Flat 2D box-and-arrow flowcharts signal low-cost commodity freelancing; bespoke 3D isometric architecture models communicate principal-level authority.

1. Visual Style Guide
---------------------

* **Backdrop**: Deep obsidian studio floor (``#000410``).
* **Perspective**: 3D isometric projection with high-depth raytracing and volumetric neon lighting (OctaneRender style).
* **Color Palette**: Electric cyan (network / data pipelines), emerald green (healthy / hardened states), warm amber/gold (cryptographic keys / legacy systems), and deep violet (identity / routing fabrics).
* **HUD Overlay**: Translucent glass holographic telemetry panels displaying real metrics, status labels, and architectural layers.

2. Media Generation & CDN Hosting
---------------------------------

* Images are synthesized via generative prompt engineering and saved to ``assets/banners/<name>.jpg``.
* Banners are committed to version control and pushed to the public GitHub repository (``https://github.com/renich/contra``).
* Assets are consumed via GitHub's raw CDN (``https://raw.githubusercontent.com/renich/contra/main/assets/banners/...``), allowing Contra's Cloudinary pipeline to ingest, optimize, and serve WebP variants automatically.

Model Context Protocol (MCP) Integration & Safety Protocol
==========================================================

The repository communicates directly with Contra's hosted remote MCP server (``https://contra.com/mcp``) via JSON-RPC 2.0.

1. Automated OAuth 2.0 Self-Healing (RFC 6749)
----------------------------------------------

Contra's OAuth bearer tokens expire every 60 minutes. Rather than blocking operations for manual browser re-authentication, `scripts/contra-cli.py <../scripts/contra-cli.py>`_ implements automated token refresh:

* When an API call receives an ``HTTP 401 Unauthorized``, the client automatically executes an RFC 6749 refresh grant against ``https://contra.com/api/mcp/oauth/token`` using the stored ``refresh_token`` and ``client_id``.
* The newly issued access and refresh tokens are atomically updated in both ``~/.gemini/antigravity-cli/mcp_oauth_tokens.json`` and ``~/.gemini/config/mcp_config.json``.
* The failed request is retried once seamlessly with the new bearer token.

2. Prepare-and-Confirm Safety Architecture
------------------------------------------

Contra MCP write operations (creating/updating services, projects, invoices, or proposals) follow a strict two-phase transaction lifecycle:

1. **Phase 1 (Prepare)**: The ``*_prepare`` tool validates inputs, creates an ephemeral server-side draft with a 900-second TTL, and returns a human-readable diff (``preview.changes`` or ``preview.summary``).
2. **Phase 2 (User Verification)**: The agent is strictly prohibited from auto-confirming. Every row of the preview diff must be displayed verbatim to the user for explicit sign-off.
3. **Phase 3 (Confirm)**: Upon explicit user confirmation, the ``*_confirm`` tool is invoked with ``{"draftId": "<uuid>", "confirm": true}``, committing the draft live to Contra.

3. Automated CLI Dispatch Tools
-------------------------------

* `scripts/contra-cli.bash <../scripts/contra-cli.bash>`_: Bash wrapper enforcing ``set -euo pipefail`` and scoped variables.
* `scripts/prepare-banner-updates.py <../scripts/prepare-banner-updates.py>`_ and `scripts/confirm-banner-updates.py <../scripts/confirm-banner-updates.py>`_: Batch automation for service and portfolio banner deployments.
* `scripts/prepare-5-new-services.py <../scripts/prepare-5-new-services.py>`_ and `scripts/confirm-5-new-services.py <../scripts/confirm-5-new-services.py>`_: Batch creation and publishing of productized services.

Lead Qualification & SOW Lifecycle
==================================

When inquiries or leads arrive through Contra or external channels, they pass through a structured qualification funnel:

1. 5-Minute Lead Triage Rubric
------------------------------

* **Technical Alignment**: Linux/Fedora/RHEL, containerization (Podman/Kubernetes), IaC (OpenTofu/Ansible), Crystal/Go/Bash, cloud or bare-metal. Reject proprietary Windows/.NET or outdated closed stacks.
* **Budget Alignment**: Minimum engagement threshold ($3,000). Reject undefined budgets or sub-market hourly requests.
* **Autonomy & Respect**: Filter for engineering leaders (CTOs, VPs, founders) who respect sovereign infrastructure and async-first communication. Reject micromanaged briefs.

2. Scope of Work (SOW) Drafting
-------------------------------

* Client proposals are modularly constructed from our approved service definitions under ``clients/<client-name>/proposal.rst``.
* Every SOW itemizes:
  
  * Context & Problem Statement
  * Proposed Technical Architecture
  * Milestones, Deliverables & Payouts
  * Verifiable Acceptance Criteria
  * Explicitly Out-of-Scope Boundaries
  * Prerequisites & Access Checklist

3. Milestone Escrow & Sign-off
------------------------------

* Work begins only after the initial milestone funds are locked in Contra's escrow.
* Deliverables are submitted with reproducible test suites, runbooks, and git commits.
* Payout release is triggered on Contra upon milestone verification, followed by automated review requests and fractional retainer proposals.

Project Journaling Protocol (PJP)
=================================

All architectural decisions, client discoveries, and state transitions are tracked persistently using ``ajourn`` (PJP):

* **Status Check**: ``ajourn status``
* **Log Architectural Decisions**: ``ajourn log -m "DEC: <decision>" -t "DEC"``
* **Log Technical Gotchas / Discoveries**: ``ajourn log -m "GOT: <discovery>" -t "GOT"``
* **State Updates**: ``ajourn state set <key> <value>``
* Routine shell commands are not micro-logged; only actionable knowledge deltas and state changes are preserved.
