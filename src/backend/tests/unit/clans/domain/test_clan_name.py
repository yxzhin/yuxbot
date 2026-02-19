import pytest

from src.backend.services.clans.domain.exceptions import InvalidClanNameLengthError
from src.backend.services.clans.domain.value_objects import ClanName


async def test_clan_name_whitespace_removal():
    name_raw = "  ril   73\t\n  "
    cn = ClanName(name_raw)
    assert " " not in cn.value
    assert "\t" not in cn.value
    assert cn.value == "ril73"


async def test_clan_name_invalid_length_raises():
    with pytest.raises(InvalidClanNameLengthError):
        ClanName("73")  # < 3

    with pytest.raises(InvalidClanNameLengthError):
        ClanName("a" * 31)  # > 30
