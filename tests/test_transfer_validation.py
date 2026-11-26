import pytest
from src.manager import Manager
from src.models import Parameters, Transfer


def test_validate_transfer_amounts():
    manager = Manager(Parameters())
    manager.min_transfer_amount = 50.0
    manager.max_transfer_amount = 5000.0

    manager.transfers = [
        Transfer(amount_pln=10.0, date="2026-01-10", settlement_year=2026, settlement_month=1, tenant="Jan Kowalski"),      # za mało
        Transfer(amount_pln=1200.0, date="2026-01-11", settlement_year=2026, settlement_month=1, tenant="Anna Nowak"),      # OK
        Transfer(amount_pln=8000.0, date="2026-01-12", settlement_year=2026, settlement_month=1, tenant="Piotr Zieliński")  # za dużo
    ]

    invalid_transfers = manager.validate_transfer_amounts()
    assert len(invalid_transfers) == 2

    invalid_amounts = [t.amount_pln for t in invalid_transfers]
    assert 10.0 in invalid_amounts
    assert 8000.0 in invalid_amounts
