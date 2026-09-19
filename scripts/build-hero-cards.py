#!/usr/bin/env python3
"""
scripts/build-hero-cards.py - Generates publication-grade 1920x1080 (16:9) Hero Showcase Cards
for Contra portfolio case studies using D2 architecture diagrams (Theme 201) and Pillow.
"""

import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

CANVAS_WIDTH = 1920
CANVAS_HEIGHT = 1080

BG_COLOR = (0, 4, 16)           # Theme 201 background #000410
CARD_BG = (7, 12, 26)           # Subtle elevated card #070c1a
BORDER_COLOR = (30, 41, 59)     # #1e293b
HEADER_COLOR = (248, 250, 252)  # #f8fafc
SUBTITLE_COLOR = (148, 163, 184) # #94a3b8
BADGE_BG = (15, 23, 42)         # #0f172a
BADGE_BORDER = (56, 189, 248)   # #38bdf8
BADGE_TEXT = (56, 189, 248)     # #38bdf8 Sky Blue
STAT_COLOR = (52, 211, 153)     # #34d399 Emerald
STAT_LABEL = (148, 163, 184)

def get_font(size, bold=False):
    font_name = "Cantarell-Bold.otf" if bold else "Cantarell-Regular.otf"
    font_path = f"/usr/share/fonts/cantarell/{font_name}"
    if not os.path.exists(font_path):
        font_path = "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf"
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        return ImageFont.load_default()

def create_hero_card(config):
    d2_source = config["d2_source"]
    output_png = config["output_png"]
    title = config["title"]
    subtitle = config["subtitle"]
    tags = config["tags"]
    kpis = config["kpis"]

    # 1. Compile D2 using Theme 201 (Dark Flagship Terrastruct)
    temp_d2_png = "/tmp/d2_temp_render.png"
    cmd = ["d2", "--theme", "201", "--pad", "20", d2_source, temp_d2_png]
    subprocess.run(cmd, check=True)

    d2_img = Image.open(temp_d2_png).convert("RGBA")

    # 2. Base 1920x1080 canvas
    canvas = Image.new("RGBA", (CANVAS_WIDTH, CANVAS_HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(canvas)

    # 3. Outer subtle frame
    draw.rounded_rectangle(
        [(16, 16), (CANVAS_WIDTH - 16, CANVAS_HEIGHT - 16)],
        radius=14,
        fill=BG_COLOR,
        outline=BORDER_COLOR,
        width=1
    )

    # 4. Header Bar
    title_font = get_font(30, bold=True)
    sub_font = get_font(17, bold=False)
    badge_font = get_font(14, bold=True)

    draw.text((50, 40), title, fill=HEADER_COLOR, font=title_font)
    draw.text((50, 82), subtitle, fill=SUBTITLE_COLOR, font=sub_font)

    # Draw Tech Badges on top-right
    badge_x = CANVAS_WIDTH - 50
    for tag in reversed(tags):
        bbox = badge_font.getbbox(tag)
        bw = (bbox[2] - bbox[0]) + 20
        bh = 28
        badge_x -= bw
        draw.rounded_rectangle(
            [(badge_x, 48), (badge_x + bw, 48 + bh)],
            radius=6,
            fill=BADGE_BG,
            outline=BADGE_BORDER,
            width=1
        )
        draw.text((badge_x + 10, 53), tag, fill=BADGE_TEXT, font=badge_font)
        badge_x -= 10

    # Header separator line
    draw.line([(50, 120), (CANVAS_WIDTH - 50, 120)], fill=(30, 41, 59), width=1)

    # 5. Center Architecture Diagram
    target_area_w = CANVAS_WIDTH - 100  # 1820 px
    target_area_h = 760                 # 760 px
    target_top = 135

    d2_w, d2_h = d2_img.size
    scale = min(target_area_w / d2_w, target_area_h / d2_h)
    new_w = int(d2_w * scale)
    new_h = int(d2_h * scale)

    resized_d2 = d2_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    paste_x = (CANVAS_WIDTH - new_w) // 2
    paste_y = target_top + (target_area_h - new_h) // 2

    canvas.paste(resized_d2, (paste_x, paste_y), resized_d2)

    # Footer separator line
    draw.line([(50, 930), (CANVAS_WIDTH - 50, 930)], fill=(30, 41, 59), width=1)

    # 6. Bottom KPI Metrics Cards
    kpi_count = len(kpis)
    total_gap = 16 * (kpi_count - 1)
    kpi_w = (target_area_w - total_gap) // kpi_count
    kpi_h = 88
    kpi_y = 952

    stat_font = get_font(24, bold=True)
    label_font = get_font(14, bold=False)

    for i, kpi in enumerate(kpis):
        kx = 50 + i * (kpi_w + 16)
        draw.rounded_rectangle(
            [(kx, kpi_y), (kx + kpi_w, kpi_y + kpi_h)],
            radius=8,
            fill=(10, 18, 36),
            outline=(30, 41, 59),
            width=1
        )
        draw.text((kx + 16, kpi_y + 14), kpi["stat"], fill=STAT_COLOR, font=stat_font)
        draw.text((kx + 16, kpi_y + 48), kpi["label"], fill=STAT_LABEL, font=label_font)

    # Save output
    canvas.save(output_png, format="PNG", optimize=True)
    print(f"Generated {output_png} (1920x1080, 16:9)")

def main():
    configs = [
        {
            "d2_source": "assets/diagrams/adip-migration.d2",
            "output_png": "assets/diagrams/adip-migration.png",
            "title": "Enterprise Cloud Migration: 4,500 Instances to OpenStack & OpenShift",
            "subtitle": "Client: ADIP (Government of Mexico City) • Migration Lead & Principal Architect",
            "tags": ["RHOSO 18", "OKD", "Ceph 9", "os-migrate", "Python/Bash"],
            "kpis": [
                {"stat": "80% Reduction", "label": "Engineering Hours Saved"},
                {"stat": "4,500+ Instances", "label": "Full Production State Migrated"},
                {"stat": "100% Data Integrity", "label": "Zero Loss of Public Records"},
                {"stat": "Under 6 Weeks", "label": "Delivered Ahead of Schedule"}
            ]
        },
        {
            "d2_source": "assets/diagrams/advantagemls-gcp.d2",
            "output_png": "assets/diagrams/advantagemls-gcp.png",
            "title": "GCP Cloud Cost Optimization & Zero-Downtime OS Modernization",
            "subtitle": "Client: AdvantageMLS • Infrastructure Manager & Cloud Systems Architect",
            "tags": ["GCP", "OpenTofu", "CentOS Stream 10", "Cloud CDN", "GitLab CI"],
            "kpis": [
                {"stat": "35% Spend Cut", "label": "Sustained Monthly GCP Savings"},
                {"stat": "$45,000+ / Year", "label": "Annualized Infrastructure ROI"},
                {"stat": "100% Uptime", "label": "Zero Downtime During OS Upgrade"},
                {"stat": ">85% Cache Hits", "label": "Edge CDN Latency Slashed by 40%"}
            ]
        },
        {
            "d2_source": "assets/diagrams/modelyo-openstack-gcp.d2",
            "output_png": "assets/diagrams/modelyo-openstack-gcp.png",
            "title": "High-Availability OpenStack Control Plane on Google Cloud Platform",
            "subtitle": "Client: Modelyo • Lead Cloud Infrastructure Architect (Solo Sprint)",
            "tags": ["OpenStack", "GCP VPC", "OpenTofu", "Dummy Interfaces", "Policy Routing"],
            "kpis": [
                {"stat": "$80,000+ Saved", "label": "Client Resource Fees Preserved"},
                {"stat": "Under 3 Weeks", "label": "Solo End-to-End Delivery"},
                {"stat": "<800ms Failover", "label": "Sub-Second Multi-Zone Redirection"},
                {"stat": "Zero Overlay Bloat", "label": "Kernel-Native Routing Architecture"}
            ]
        },
        {
            "d2_source": "assets/diagrams/cloudsigma-kvm.d2",
            "output_png": "assets/diagrams/cloudsigma-kvm.png",
            "title": "Global Virtualization Scaling: 150,000+ VMs & Podman S3 Storage",
            "subtitle": "Client: CloudSigma • Senior Systems Administrator & Infrastructure Lead",
            "tags": ["KVM / QEMU", "Libvirt", "Podman", "Minio S3", "SELinux"],
            "kpis": [
                {"stat": "150,000+ VMs", "label": "Global Multi-Tenant Fleet Density"},
                {"stat": "99.95% Availability", "label": "Across 10 International Datacenters"},
                {"stat": "+40% Throughput", "label": "S3 Storage Read/Write Boost"},
                {"stat": "Zero VM Escapes", "label": "SELinux Type Enforcement Isolation"}
            ]
        }
    ]

    for cfg in configs:
        create_hero_card(cfg)

if __name__ == "__main__":
    main()
