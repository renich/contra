======================================================
Visual Media, Diagramming & Video Strategy for Contra
======================================================

:Author: René (Rénich) Bon Ćirić & Antigravity AI
:Date: 2026-09-19
:Context: High-Conversion Portfolio & Case Study Presentation

.. contents:: Table of Contents
   :depth: 2

The Engineering Visual Formula on Contra
========================================

Contra is a design-centric, visually-forward platform originally popularized by digital designers and now dominant among elite engineering freelancers and fractional leaders.

On Contra, text-only case studies suffer low engagement. However, for a Principal Infrastructure Architect, **using generic stock photos of server racks or glowing blue circuit boards destroys credibility**.

The winning visual aesthetic for high-end infrastructure and systems architecture combines four distinct artifact tiers:

#. **Dark-Mode Architecture Schematics**: High-contrast, clean system topology diagrams authored in declarative D2 code.
#. **Animated Terminal Demos (GIF/WebM)**: Fast, crisp terminal screen captures showing automation scripts, compiler passes, and deployment pipelines in action.
#. **Verifiable Dashboard Snapshots**: Clean screenshots of real production metrics (Grafana latency drop, GCP billing decline curve, GitLab CI pipeline DAGs).
#. **Async Video Postmortems (60–90 Seconds)**: High-production Loom/screencast walkthroughs breaking down the problem, the architecture, and the outcome.

Asset Specifications & Dimensions
=================================

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 40

   * - Asset Type
     - Recommended Size
     - Aspect Ratio
     - Ideal Format

   * - Project Hero Banner
     - 1920x1080 px
     - 16:9
     - PNG / WebP (Dark theme, D2 rendered or stylized SVG)

   * - Service Card Preview
     - 1200x800 px
     - 3:2
     - PNG / WebP (Clean visual iconography or system schematic)

   * - Inline Architecture Diagram
     - 1600x900 px
     - 16:9 or Flexible
     - SVG (vector) or 2x PNG

   * - Terminal Session Animation
     - 1280x720 px
     - 16:9
     - GIF (dithered) or WebM/MP4 (under 10MB)

   * - Case Study Video Walkthrough
     - 1080p (60fps)
     - 16:9
     - MP4 (H.264 / AAC) or Loom/YouTube embed

Tooling Recipes on Fedora Linux
===============================

1. Declarative Architecture Diagrams with D2
--------------------------------------------

D2 (``/usr/bin/d2``) produces publication-quality architecture diagrams directly from version-controlled code.

**Compilation Command**:

.. code-block:: bash

   # Render high-resolution PNG with dark mauve theme
   d2 --theme 200 --pad 20 assets/diagrams/modelyo-openstack-gcp.d2 assets/diagrams/modelyo-openstack-gcp.png

   # Render scalable SVG for crisp high-DPI rendering
   d2 --theme 200 --pad 20 assets/diagrams/modelyo-openstack-gcp.d2 assets/diagrams/modelyo-openstack-gcp.svg

**Best Practice**: Store source ``.d2`` files in ``assets/diagrams/`` and compile them automatically via ``scripts/build-diagrams.bash``.

2. Animated Terminal Sessions with asciinema & ffmpeg
-----------------------------------------------------

To demonstrate tools like ``crinit``, ``shellmin``, ``wa-cli``, or ``pjp`` in action without bloated video players:

#. **Record clean terminal session**:

   .. code-block:: bash

      asciinema rec --overwrite session.cast
      # Execute target workflow (e.g. crinit build, make test, pjp status)
      exit

#. **Convert to high-framerate GIF / MP4**:

   .. code-block:: bash

      # Generate paletted high-quality GIF using ffmpeg
      ffmpeg -i session.cast -vf "fps=15,scale=1280:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" session.gif

3. Wayland-Native Screencasting (Kooha & OBS Studio)
----------------------------------------------------

For short async case study videos on Fedora Wayland:

* **Kooha**: Lightweight GNOME Wayland recorder. Supports direct GIF, WebM, and MP4 capture with custom audio input selection.
* **OBS Studio (PipeWire)**: Professional screen capture with webcam overlay ("talking head") and high-end microphone audio processing.

60-Second Video Walkthrough Blueprint
=====================================

A 60-second video walkthrough on Contra drastically increases client trust and conversion. Structure each video with this exact 4-part pacing:

#. **00:00 – 00:10 (The Problem & Stakes)**:
   
   *"When Modelyo needed to run a private cloud inside Google Cloud Platform, the project was blocked because GCP's VPC doesn't support Layer-2 broadcast or Keepalived VIPs."*

#. **00:10 – 00:35 (The Architecture Walkthrough)**:
   
   *(Pan over the D2 architecture diagram)*:
   *"Instead of paying for third-party SDN overlays, I designed a native routing architecture using Linux dummy interfaces combined with GCP internal load balancers and custom routing rules."*

#. **00:35 – 00:50 (The Live Proof)**:
   
   *(Cut to terminal or console)*:
   *"Here you can see the automated failover test: when the primary controller goes down, health-check probes redirect API traffic in under 800 milliseconds without dropping state."*

#. **00:50 – 01:00 (The Verifiable Outcome)**:
   
   *"The result: a fully operational HA OpenStack control plane delivered solo in under 3 weeks, saving the client over $80,000 in engineering costs."*

Recommended Visual Assets Per Case Study
========================================

ADIP (4,500 OpenStack Instances)
--------------------------------

* **Hero Banner**: High-level migration bridge diagram showing RHOSP 16.2 to RHOSO 18 over Ceph 9.
* **Inline Diagram**: Migration wave batching sequence (Pre-flight -> Volume Snapshot -> Ceph Pool Sync -> Validation).
* **Terminal GIF**: Orchestrator executing automated pre-flight checks and ``os-migrate`` serialization.

AdvantageMLS (GCP Cost Optimization)
------------------------------------

* **Hero Banner**: Modernized GCP architecture diagram featuring OpenTofu, CDN edge caching, and CentOS Stream 10 nodes.
* **Metric Visual**: Graph showcasing the 35% spend drop ($45k+ annualized savings) post-optimization.
* **Terminal GIF**: Modular OpenTofu drift detection and automated plan execution.

Modelyo (OpenStack on GCP VPC)
------------------------------

* **Hero Banner**: Custom L2/L3 dummy interface and GCP Internal Load Balancer routing topology.
* **Inline Diagram**: Sub-second failover state machine across multi-zone GCP compute instances.
* **Terminal GIF**: Simulated node kill and instant API VIP failover verification.

CloudSigma (150,000+ Tenant VMs)
--------------------------------

* **Hero Banner**: Global 10-datacenter KVM/QEMU hypervisor architecture with Podman S3 storage.
* **Inline Diagram**: Memory-backed host isolation and SELinux Type Enforcement containment model.
* **Terminal GIF**: Podman Quadlet service management under systemd.
