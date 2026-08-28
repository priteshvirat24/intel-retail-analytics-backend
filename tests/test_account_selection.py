"""
Unit tests for app.models.account_selection (AccountSelectionManager).
Tests:
1. 63-capacity master catalog validation (52 confirmed baseline + 11 awaiting definition slots).
2. Point-in-time monthly snapshot creation.
3. Automated carry-forward when no change request is provided.
4. Client change request application (updating frequency, defining pending slots, activating/deactivating).
5. Strict historical immutability (modifications to Month 3 do not alter Month 1 or Month 2).
"""
import pytest
from pathlib import Path
from app.models.account_selection import AccountSelectionManager


def test_master_catalog_capacity_and_placeholder_slots(tmp_path):
    ledger_file = tmp_path / "test_monthly_selections.json"
    mgr = AccountSelectionManager(ledger_path=ledger_file)
    
    summary = mgr.get_catalog_summary()
    assert summary["total_contractual_capacity"] == 63
    assert summary["confirmed_baseline_accounts"] == 52
    assert summary["pending_client_definition_slots"] == 11
    assert len(summary["unassigned_slots"]) == 11
    assert "SLOT_53_AWAITING_DEFINITION" in summary["unassigned_slots"]
    assert "SLOT_63_AWAITING_DEFINITION" in summary["unassigned_slots"]


def test_four_month_simulation_carry_forward_and_immutability(tmp_path):
    ledger_file = tmp_path / "monthly_ledger.json"
    mgr = AccountSelectionManager(ledger_path=ledger_file)

    # -------------------------------------------------------------------------
    # MONTH 1: 2026-08 (Initial Baseline)
    # -------------------------------------------------------------------------
    m1 = mgr.get_or_create_monthly_selection("2026-08")
    assert m1["month"] == "2026-08"
    assert m1["status"] == "BASELINE_INITIALIZED"
    assert m1["active_accounts_count"] == 52
    assert len(m1["pending_slots"]) == 11
    assert m1["active_accounts"]["Best Buy - US"]["tracking_frequency"] == "Monthly"
    assert m1["active_accounts"]["Best Buy - US"]["active"] is True

    # -------------------------------------------------------------------------
    # MONTH 2: 2026-09 (No Change Request -> Carry-Forward from Month 1)
    # -------------------------------------------------------------------------
    m2 = mgr.get_or_create_monthly_selection("2026-09")
    assert m2["month"] == "2026-09"
    assert m2["status"] == "ACTIVE_CARRIED_FORWARD"
    assert m2["derived_from"] == "2026-08"
    assert m2["active_accounts_count"] == 52
    assert m2["active_accounts"]["Best Buy - US"]["tracking_frequency"] == "Monthly"
    assert len(m2["pending_slots"]) == 11

    # -------------------------------------------------------------------------
    # MONTH 3: 2026-10 (Change Request Applied)
    # Changes:
    # 1. Update Best Buy - US frequency from 'Monthly' to 'Once per quarter'
    # 2. Deactivate 'Acer' for this cycle
    # 3. Assign SLOT_53 to newly specified account 'Client Custom Store - UK'
    # -------------------------------------------------------------------------
    changes_m3 = {
        "Best Buy - US": {
            "tracking_frequency": "Once per quarter"
        },
        "Acer": {
            "active": False
        },
        "SLOT_53": {
            "assign_slot": "SLOT_53",
            "account_name": "Client Custom Store - UK",
            "country": "United Kingdom",
            "account_type": "1P Retailer",
            "tracking_frequency": "Monthly",
            "active": True
        }
    }

    m3 = mgr.apply_change_request(
        month="2026-10",
        account_updates=changes_m3,
        change_request_id="CR-2026-10-INTEL-001",
        notes="Q4 scope adjustments: added UK custom store, changed Best Buy frequency, paused Acer."
    )

    assert m3["month"] == "2026-10"
    assert m3["status"] == "CHANGE_REQUEST_APPLIED"
    assert m3["change_request_id"] == "CR-2026-10-INTEL-001"
    assert m3["active_accounts"]["Best Buy - US"]["tracking_frequency"] == "Once per quarter"
    assert m3["active_accounts"]["Acer"]["active"] is False
    assert "Client Custom Store - UK" in m3["active_accounts"]
    assert m3["active_accounts"]["Client Custom Store - UK"]["active"] is True
    # 52 baseline - 1 (Acer deactivated) + 1 (SLOT_53 activated) = 52 active
    assert m3["active_accounts_count"] == 52

    # Verify SLOT_53 is now marked ASSIGNED
    slot_53 = [s for s in m3["pending_slots"] if s["slot_id"] == "SLOT_53"][0]
    assert slot_53["status"] == "ASSIGNED"
    assert slot_53["assigned_account"] == "Client Custom Store - UK"

    # -------------------------------------------------------------------------
    # MONTH 4: 2026-11 (No Change Request -> Carry-Forward from Month 3)
    # -------------------------------------------------------------------------
    m4 = mgr.get_or_create_monthly_selection("2026-11")
    assert m4["month"] == "2026-11"
    assert m4["status"] == "ACTIVE_CARRIED_FORWARD"
    assert m4["derived_from"] == "2026-10"
    # Carries forward Month 3 changes:
    assert m4["active_accounts"]["Best Buy - US"]["tracking_frequency"] == "Once per quarter"
    assert m4["active_accounts"]["Acer"]["active"] is False
    assert "Client Custom Store - UK" in m4["active_accounts"]
    assert m4["active_accounts"]["Client Custom Store - UK"]["active"] is True
    assert m4["active_accounts_count"] == 52

    # -------------------------------------------------------------------------
    # IMMUTABILITY VERIFICATION: Re-read Month 1 and Month 2 from disk
    # -------------------------------------------------------------------------
    mgr_fresh = AccountSelectionManager(ledger_path=ledger_file)
    m1_fresh = mgr_fresh.get_or_create_monthly_selection("2026-08")
    m2_fresh = mgr_fresh.get_or_create_monthly_selection("2026-09")

    # Month 1 remains pristine
    assert m1_fresh["active_accounts"]["Best Buy - US"]["tracking_frequency"] == "Monthly"
    assert m1_fresh["active_accounts"]["Acer"]["active"] is True
    assert "Client Custom Store - UK" not in m1_fresh["active_accounts"]
    assert m1_fresh["status"] == "BASELINE_INITIALIZED"

    # Month 2 remains pristine
    assert m2_fresh["active_accounts"]["Best Buy - US"]["tracking_frequency"] == "Monthly"
    assert m2_fresh["active_accounts"]["Acer"]["active"] is True
    assert "Client Custom Store - UK" not in m2_fresh["active_accounts"]
    assert m2_fresh["status"] == "ACTIVE_CARRIED_FORWARD"

    # Verify audit trail contains the change request record
    trail = mgr_fresh.get_audit_trail()
    assert len(trail) == 1
    assert trail[0]["change_request_id"] == "CR-2026-10-INTEL-001"
    assert trail[0]["month"] == "2026-10"
