=================================================
Contra Platform Mechanics & Operational Playbook
=================================================

:Author: René (Rénich) Bon Ćirić & Antigravity AI
:Date: 2026-09-19
:Context: Platform Operations, Escrow & Client Management

.. contents:: Table of Contents
   :depth: 2

Platform Philosophy & Business Model
====================================

`Contra <https://contra.com>`_ is designed as an independent professional network rather than a race-to-the-bottom gig broker.

Key economic advantages:

* **0% Commission on Freelancer Earnings**: Contra does not take a 10%–20% cut from freelancer fees (unlike Upwork or Fiverr).
* **Escrow Protection**: Clients fund milestones in advance. Escrow protects contractor labor before code or configuration changes commence.
* **Modern Productization**: Emphasizes packaged services, structured case studies, and recurring retainers over unconstrained hourly billing.

Core Platform Primitives
========================

1. Projects (Portfolio Case Studies)
------------------------------------

Projects serve as proof-of-work showrooms. On Contra:

* Projects are media-rich: they combine hero cover images, inline architecture diagrams, code blocks, and embedded demo videos.
* Each project links directly to the relevant **Services** offered.
* High-performing projects clearly highlight verifiable metrics (e.g. 35% cost reduction, 4,500 instances migrated, 99.95% uptime).

2. Services (Packaged Offerings)
--------------------------------

Services allow clients to hire you instantly for a predefined scope:

* **Fixed Price**: Standardized discovery audits, compliance reviews, or container migrations with defined delivery windows (e.g. 5–7 days).
* **Flexible Milestones**: Multi-phase engagements where each phase requires separate client escrow funding.
* **Monthly / Weekly Retainers**: Fractional principal SRE advisory, ongoing platform governance, and architecture steering.

3. Inquiries & Custom Proposals
-------------------------------

When an inbound lead contacts you or posts a brief:

* Use our `Client Intake Rubric <../proposals/intake-rubric.rst>`_ to qualify the opportunity in under 5 minutes.
* Generate a modular proposal from our `SOW Template <../proposals/sow-template.rst>`_.
* Submit the proposal directly through Contra's proposal builder, defining exact milestone dates, escrow sums, and acceptance criteria.

Contra Escrow & Payment Lifecycle
=================================

.. code-block:: text

   [Proposal Accepted] -> [Client Funds Milestone 1 Escrow] -> [Work Commences]
           |
           v
   [Deliverable Delivered & Tested] -> [Milestone Completion Submitted on Contra]
           |
           v
   [Client Reviews Deliverable] -> [Escrow Released to Bank / Stripe]
           |
           v
   [Client Funds Milestone 2 Escrow] -> [Phase 2 Commences]

Critical Contract Rules
-----------------------

#. **Never commence work before escrow is funded**: Work on any phase begins strictly after Contra confirms milestone funding.
#. **Explicit Acceptance Window**: Proposals must include a standard 5 business day acceptance clause (if no formal objection is raised, deliverable is deemed accepted).
#. **Scope Creep Boundary**: Any request outside the itemized deliverables requires a new milestone amendment or converts into an ongoing advisory retainer.

Profile Ranking & Conversion Optimization
=========================================

To maximize algorithmic visibility and conversion on Contra:

* **Fast Response Time**: Maintain a median response time under 2 hours for inbound inquiries.
* **Client Recommendations**: Request verified reviews and recommendations immediately following milestone closeout.
* **Visual Density**: Ensure every featured case study has a custom D2 diagram hero banner and clear metric callouts.
* **Direct Links**: Promote your Contra profile URL across your technical blog (`blog.woralelandia.com <https://blog.woralelandia.com>`_) and consulting site (`evalinux.com <https://evalinux.com>`_).
