import pytest

from src.backend.services.clans.domain.exceptions import (
    InvalidClanTagLengthError,
    InvalidClanTagValueError,
)
from src.backend.services.clans.domain.value_objects import ClanTag


async def test_clan_tag_whitespace_removal_and_upper():
    tag_raw = "   73\n\t  "
    ct = ClanTag(tag_raw)
    assert ct.value == "73"


async def test_clan_tag_invalid_length_raises():
    with pytest.raises(InvalidClanTagLengthError):
        ClanTag("A")  # < 2

    with pytest.raises(InvalidClanTagLengthError):
        ClanTag("ABCDEFG")  # > 6

    with pytest.raises(InvalidClanTagValueError):
        ClanTag("ABСDЁ")  # contains non-ascii
