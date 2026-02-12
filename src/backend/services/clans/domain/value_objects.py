from dataclasses import dataclass
from string import whitespace

from .exceptions import (
    InvalidClanNameLengthError,
    InvalidClanTagLengthError,
    InvalidClanTagValueError,
)


@dataclass
class ClanName:
    value: str

    def __post_init__(self):
        trans = str.maketrans("", "", whitespace)
        self.value = self.value.translate(trans)

        if 3 > len(self.value) > 30:
            raise InvalidClanNameLengthError(
                "clan name length must be 3-30 characters long"
            )


@dataclass
class ClanTag:
    value: str

    def __post_init__(self):
        trans = str.maketrans("", "", whitespace)
        self.value = self.value.capitalize().translate(trans)

        if 2 > len(self.value) > 6:
            raise InvalidClanTagLengthError(
                "clan tag length must be 2-6 characters long"
            )

        if not self.value.isascii():
            raise InvalidClanTagValueError(
                "clan tag must contain only ascii characters"
            )
