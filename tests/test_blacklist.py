import json
import pytest
from src.manager import Manager
from src.models import Parameters, BlacklistedTenant

def test_tenant_is_on_blacklist(tmp_path):
    blacklist_file = tmp_path / "blacklist.json"
    data = [
        {"name": "Jan Kowalski", "reason": "Zaległości w czynszu przez 6 miesięcy"},
        {"name": "Anna Nowak", "reason": "Zniszczenie wyposażenia"}
    ]
    blacklist_file.write_text(json.dumps(data), encoding="utf-8")

    params = Parameters()
    params.blacklist_json_path = str(blacklist_file)
    manager = Manager(params)

    result = manager.is_tenant_blacklisted("Jan Kowalski")
    assert isinstance(result, BlacklistedTenant)
    assert result.name == "Jan Kowalski"
    assert result.reason == "Zaległości w czynszu przez 6 miesięcy"

def test_tenant_is_not_on_blacklist(tmp_path):
    blacklist_file = tmp_path / "blacklist.json"
    data = [{"name": "Jan Kowalski", "reason": "Zaległości w czynszu"}]
    blacklist_file.write_text(json.dumps(data), encoding="utf-8")

    params = Parameters()
    params.blacklist_json_path = str(blacklist_file)
    manager = Manager(params)

    result = manager.is_tenant_blacklisted("Piotr Wiśniewski")
    assert result is None