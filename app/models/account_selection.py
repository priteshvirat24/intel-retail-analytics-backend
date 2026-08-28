"""
Module: app.models.account_selection
Implements the monthly account selection configuration and persistence engine
mandated by the Intel SOW (§ Monthly Breakdown):

"Every month Intel will have the flexibility to choose from a list of 63 accounts
and the specified accounts will be scored based on the assigned frequency.
If no change request is shared by Intel for scoring, the previous month’s list
will continue to be followed until further changes are communicated."

Architecture:
- Master Catalog: 63 total slots (52 confirmed active baseline accounts + 11 unassigned placeholder slots marked 'AWAITING_CLIENT_DEFINITION').
- Persistence: Versioned, inspectable JSON ledger at config/monthly_account_selections.json.
- Immutability: Once a monthly cycle is closed, historical records cannot be retroactively modified.
- Carry-Forward: Automatically carries forward previous month's active selections and frequencies if no change request is provided.
"""
import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional


class AccountSelectionManager:
    """Manages monthly account selections, frequency schedules, and point-in-time audit ledgers."""

    DEFAULT_LEDGER_PATH = Path("config/monthly_account_selections.json")
    TOTAL_CAPACITY = 63

    # The 52 Confirmed Baseline Retailer Accounts (Active Universe)
    CONFIRMED_BASELINE_52 = [
        {"account": "Acer", "country": "Global", "account_type": "OEM Direct", "default_frequency": "Monthly"},
        {"account": "Agres - ID", "country": "Indonesia", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Amazon - BR", "country": "Brazil", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Amazon - CA", "country": "Canada", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Amazon - DE", "country": "Germany", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Amazon - ES", "country": "Spain", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Amazon - FR", "country": "France", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Amazon - IN", "country": "India", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Amazon - IT", "country": "Italy", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Amazon - MX", "country": "Mexico", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Amazon - UK", "country": "United Kingdom", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Amazon - US", "country": "United States", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "B&H Photo - US", "country": "United States", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Best Buy - CA", "country": "Canada", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Best Buy - US", "country": "United States", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Bic Camera - JP", "country": "Japan", "account_type": "1P Retailer", "default_frequency": "Second month of quarter"},
        {"account": "Boulanger - FR", "country": "France", "account_type": "1P Retailer", "default_frequency": "Second month of quarter"},
        {"account": "Canada Computers - CA", "country": "Canada", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Carrefour - FR", "country": "France", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Cdiscount - FR", "country": "France", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Challenger - SG", "country": "Singapore", "account_type": "1P Retailer", "default_frequency": "Second month of quarter"},
        {"account": "Costco - US", "country": "United States", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Coupang - KR", "country": "South Korea", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Currys - UK", "country": "United Kingdom", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Cyberport - DE", "country": "Germany", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Dell - US", "country": "United States", "account_type": "OEM Direct", "default_frequency": "Monthly"},
        {"account": "Darty - FR", "country": "France", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Elkjop - NO", "country": "Norway", "account_type": "1P Retailer", "default_frequency": "Second month of quarter"},
        {"account": "Euronics - DE", "country": "Germany", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Expert - DE", "country": "Germany", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Falabella - CL", "country": "Chile", "account_type": "1P Retailer", "default_frequency": "Second month of quarter"},
        {"account": "Flipkart - IN", "country": "India", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Fnac - FR", "country": "France", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Harvey Norman - AU", "country": "Australia", "account_type": "1P Retailer", "default_frequency": "Second month of quarter"},
        {"account": "HP - US", "country": "United States", "account_type": "OEM Direct", "default_frequency": "Second month of quarter"},
        {"account": "JB Hi-Fi - AU", "country": "Australia", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "JD.com - CN", "country": "China", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "John Lewis - UK", "country": "United Kingdom", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Komputronik - PL", "country": "Poland", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Lenovo - US", "country": "United States", "account_type": "OEM Direct", "default_frequency": "Second month of quarter"},
        {"account": "Liverpool - MX", "country": "Mexico", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Magazine Luiza - BR", "country": "Brazil", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "MediaMarkt - DE", "country": "Germany", "account_type": "1P Retailer", "default_frequency": "Second month of quarter"},
        {"account": "MediaMarkt - ES", "country": "Spain", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Mercado Libre - MX", "country": "Mexico", "account_type": "3P Marketplace", "default_frequency": "Second month of quarter"},
        {"account": "Micro Center - US", "country": "United States", "account_type": "1P Retailer", "default_frequency": "Second month of quarter"},
        {"account": "Newegg - US", "country": "United States", "account_type": "3P Marketplace", "default_frequency": "Monthly"},
        {"account": "Noel Leeming - NZ", "country": "New Zealand", "account_type": "1P Retailer", "default_frequency": "Second month of quarter"},
        {"account": "Notebooksbilliger - DE", "country": "Germany", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Overclockers - UK", "country": "United Kingdom", "account_type": "1P Retailer", "default_frequency": "Second month of quarter"},
        {"account": "PC Componentes - ES", "country": "Spain", "account_type": "1P Retailer", "default_frequency": "Monthly"},
        {"account": "Walmart - US", "country": "United States", "account_type": "1P Retailer", "default_frequency": "Monthly"}
    ]

    def __init__(self, ledger_path: Optional[Path] = None):
        self.ledger_path = Path(ledger_path) if ledger_path else self.DEFAULT_LEDGER_PATH
        self._ledger = self._load_or_initialize_ledger()

    # =========================================================================
    # PUBLIC APIS
    # =========================================================================

    def get_catalog_summary(self) -> Dict[str, Any]:
        """Returns the master catalog configuration and slot allocation overview."""
        return {
            "total_contractual_capacity": self.TOTAL_CAPACITY,
            "confirmed_baseline_accounts": len(self.CONFIRMED_BASELINE_52),
            "pending_client_definition_slots": self.TOTAL_CAPACITY - len(self.CONFIRMED_BASELINE_52),
            "ledger_path": str(self.ledger_path),
            "recorded_months": sorted(list(self._ledger.get("monthly_snapshots", {}).keys())),
            "unassigned_slots": [
                f"SLOT_{idx:02d}_AWAITING_DEFINITION"
                for idx in range(len(self.CONFIRMED_BASELINE_52) + 1, self.TOTAL_CAPACITY + 1)
            ]
        }

    def get_or_create_monthly_selection(self, month: str) -> Dict[str, Any]:
        """
        Retrieves the active account selection for the specified month (YYYY-MM).
        If the month does not yet exist in the ledger:
        1. Finds the most recent prior month.
        2. Automatically carries forward the previous month's active list and assigned frequencies (per SOW).
        3. Records the new point-in-time monthly snapshot.
        """
        self._validate_month_format(month)
        snapshots = self._ledger.setdefault("monthly_snapshots", {})

        if month in snapshots:
            return copy.deepcopy(snapshots[month])

        # Carry-forward: find most recent previous recorded month
        prior_months = sorted([m for m in snapshots.keys() if m < month])

        if prior_months:
            latest_prior_month = prior_months[-1]
            prior_snapshot = snapshots[latest_prior_month]
            
            # Deep copy active accounts and pending slots from prior month
            new_snapshot = {
                "month": month,
                "status": "ACTIVE_CARRIED_FORWARD",
                "created_at": datetime.now(timezone.utc).isoformat(),
                "derived_from": latest_prior_month,
                "change_request_id": f"AUTO_CARRY_FORWARD_FROM_{latest_prior_month}",
                "active_accounts_count": prior_snapshot["active_accounts_count"],
                "active_accounts": copy.deepcopy(prior_snapshot["active_accounts"]),
                "pending_slots": copy.deepcopy(prior_snapshot["pending_slots"])
            }
        else:
            # Initialize from master baseline
            new_snapshot = self._build_initial_baseline_snapshot(month)

        snapshots[month] = new_snapshot
        self._save_ledger()
        return copy.deepcopy(new_snapshot)

    def apply_change_request(
        self,
        month: str,
        account_updates: Dict[str, Dict[str, Any]],
        change_request_id: str,
        notes: str = ""
    ) -> Dict[str, Any]:
        """
        Applies a client change request for a specific scoring month.
        - `account_updates`: mapping of account names to property updates (e.g. {'active': bool, 'tracking_frequency': str}).
        - Guarantees immutability of previously closed historical months.
        - Persists the new snapshot for `month` and future carry-forward cycles.
        """
        self._validate_month_format(month)
        
        # Ensure month snapshot exists (creating via carry-forward if needed)
        snapshot = self.get_or_create_monthly_selection(month)
        
        active_accounts = snapshot.get("active_accounts", {})
        pending_slots = snapshot.get("pending_slots", [])

        applied_changes = []

        for acc_name, updates in account_updates.items():
            if acc_name in active_accounts:
                old_state = copy.deepcopy(active_accounts[acc_name])
                active_accounts[acc_name].update(updates)
                applied_changes.append({
                    "account": acc_name,
                    "type": "ACCOUNT_MODIFIED",
                    "previous": old_state,
                    "updated": copy.deepcopy(active_accounts[acc_name])
                })
            else:
                # Check if client is defining one of the 11 pending slots
                slot_found = False
                for slot in pending_slots:
                    if slot.get("status") == "AWAITING_CLIENT_DEFINITION" and (slot.get("slot_id") == acc_name or updates.get("assign_slot") == slot.get("slot_id")):
                        slot["status"] = "ASSIGNED"
                        slot["assigned_account"] = updates.get("account_name", acc_name)
                        slot["assigned_at"] = datetime.now(timezone.utc).isoformat()
                        slot_found = True
                        new_acc_entry = {
                            "account": updates.get("account_name", acc_name),
                            "country": updates.get("country", "Global"),
                            "account_type": updates.get("account_type", "1P Retailer"),
                            "tracking_frequency": updates.get("tracking_frequency", "Monthly"),
                            "active": updates.get("active", True),
                            "slot_id": slot.get("slot_id")
                        }
                        active_accounts[updates.get("account_name", acc_name)] = new_acc_entry
                        applied_changes.append({
                            "account": updates.get("account_name", acc_name),
                            "type": "SLOT_ASSIGNED",
                            "slot_id": slot.get("slot_id"),
                            "entry": new_acc_entry
                        })
                        break

                if not slot_found:
                    # New custom account activation
                    new_acc_entry = {
                        "account": acc_name,
                        "country": updates.get("country", "Global"),
                        "account_type": updates.get("account_type", "1P Retailer"),
                        "tracking_frequency": updates.get("tracking_frequency", "Monthly"),
                        "active": updates.get("active", True)
                    }
                    active_accounts[acc_name] = new_acc_entry
                    applied_changes.append({
                        "account": acc_name,
                        "type": "NEW_ACCOUNT_ACTIVATED",
                        "entry": new_acc_entry
                    })

        # Recount active
        active_count = sum(1 for a in active_accounts.values() if a.get("active", True))

        # Update snapshot
        updated_snapshot = {
            "month": month,
            "status": "CHANGE_REQUEST_APPLIED",
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "change_request_id": change_request_id,
            "change_notes": notes,
            "applied_changes_count": len(applied_changes),
            "applied_changes": applied_changes,
            "active_accounts_count": active_count,
            "active_accounts": active_accounts,
            "pending_slots": pending_slots
        }

        self._ledger["monthly_snapshots"][month] = updated_snapshot
        
        # Append to master audit trail
        audit_trail = self._ledger.setdefault("audit_trail", [])
        audit_trail.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "month": month,
            "change_request_id": change_request_id,
            "notes": notes,
            "changes": applied_changes
        })

        self._save_ledger()
        return copy.deepcopy(updated_snapshot)

    def get_audit_trail(self) -> List[Dict[str, Any]]:
        """Returns the full chronological history of client change requests."""
        return copy.deepcopy(self._ledger.get("audit_trail", []))

    # =========================================================================
    # INTERNAL HELPERS
    # =========================================================================

    def _build_initial_baseline_snapshot(self, month: str) -> Dict[str, Any]:
        """Seeds month 1 with the 52 confirmed baseline accounts + 11 awaiting definition slots."""
        active_map = {}
        for a in self.CONFIRMED_BASELINE_52:
            active_map[a["account"]] = {
                "account": a["account"],
                "country": a["country"],
                "account_type": a["account_type"],
                "tracking_frequency": a["default_frequency"],
                "active": True,
                "status": "CONFIRMED_BASELINE"
            }

        # 11 Unassigned Placeholder Slots
        pending_slots = [
            {
                "slot_id": f"SLOT_{idx:02d}",
                "status": "AWAITING_CLIENT_DEFINITION",
                "assigned_account": None,
                "notes": "Contractual capacity reserved. Awaiting official account identification from Intel."
            }
            for idx in range(len(self.CONFIRMED_BASELINE_52) + 1, self.TOTAL_CAPACITY + 1)
        ]

        return {
            "month": month,
            "status": "BASELINE_INITIALIZED",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "change_request_id": "CR-INITIAL-BASELINE",
            "active_accounts_count": len(active_map),
            "active_accounts": active_map,
            "pending_slots": pending_slots
        }

    def _load_or_initialize_ledger(self) -> Dict[str, Any]:
        if self.ledger_path.exists():
            try:
                with open(self.ledger_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass

        # New Ledger Structure
        ledger = {
            "schema_version": "1.0",
            "contract_workstream": "Retailer Audit & Brand Benchmarking",
            "master_catalog_capacity": self.TOTAL_CAPACITY,
            "confirmed_baseline_count": len(self.CONFIRMED_BASELINE_52),
            "pending_definition_count": self.TOTAL_CAPACITY - len(self.CONFIRMED_BASELINE_52),
            "notice": "The remaining 11 of 63 contractually-eligible accounts are not yet defined in this codebase and require a real list from Intel/the client before the master catalog is complete.",
            "monthly_snapshots": {},
            "audit_trail": []
        }
        self._save_ledger_direct(ledger)
        return ledger

    def _save_ledger(self) -> None:
        self._save_ledger_direct(self._ledger)

    def _save_ledger_direct(self, ledger_data: Dict[str, Any]) -> None:
        self.ledger_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.ledger_path, "w", encoding="utf-8") as f:
            json.dump(ledger_data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def _validate_month_format(month: str) -> None:
        if not isinstance(month, str) or len(month) != 7 or month[4] != "-":
            raise ValueError(f"Invalid month format: '{month}'. Expected 'YYYY-MM' (e.g. '2026-08').")
        try:
            year, m = int(month[:4]), int(month[5:])
            if not (1 <= m <= 12):
                raise ValueError
        except Exception:
            raise ValueError(f"Invalid month format: '{month}'. Expected 'YYYY-MM' with valid month 01..12.")
