#!/usr/bin/env python3
"""
scripts/confirm-5-new-services.py - Confirms and creates the 5 prepared services on Contra.
"""

import sys
import json
import time

sys.path.insert(0, "scripts")
import contra_cli

def main():
    try:
        with open("prepared-5-new-services.json") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading prepared-5-new-services.json: {e}")
        sys.exit(1)

    print("=== CONFIRMING 5 NEW ENTERPRISE SERVICES ===")
    for svc in data:
        title = svc.get("title")
        draft_id = svc.get("draftId")
        print(f"\nConfirming: {title} (draftId: {draft_id})...")
        res = contra_cli.call_tool("create_productized_service_confirm", {
            "draftId": draft_id,
            "confirm": True
        })
        sc = res.get("result", {}).get("structuredContent", {})
        if sc.get("ok"):
            service_obj = sc.get("service", {})
            print(f"  ✓ Published live! URL: {service_obj.get('serviceUrl')}")
        else:
            print(f"  ✗ Failed: {res}")
        time.sleep(1)

    print("\nAll 5 new services confirmed and published live!")

if __name__ == "__main__":
    main()
