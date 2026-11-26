import pytest
from src.manager import Manager
from src.parameters import Parameters
from src.models import Transfer

def test_validate_transfer_amounts():
    manager = Manager(Parameters())
    manager.min_transfer_amount = 50.0
    manager.max_transfer_amount = 5000.0

    manager.transfers = [
        Transfer(amount=10.0, tenant="Jan Kowalski", date="2026-01-10"),    # za mało
        Transfer(amount=1200.0, tenant="Anna Nowak", date="2026-01-11"),    # OK
        Transfer(amount=8000.0, tenant="Piotr Zieliński", date="2026-01-12") # za dużo
    ]

    invalid_transfers = manager.validate_transfer_amounts()
    assert len(invalid_transfers) == 2
    amounts = [t.amount for t in invalid_transfers]
    assert 10.0 in amounts
    assert 8000.0 in amounts