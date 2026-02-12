from sqlalchemy.types import STRINGTYPE, TypeDecorator

from ...domain.value_objects import ClanName


class ClanNameMapper(TypeDecorator):
    impl = STRINGTYPE

    def process_bind_param(self, clan_name: ClanName | None, dialect) -> str | None:
        if clan_name is None:
            return None
        return clan_name.value

    def process_result_value(self, value: str | None, dialect) -> ClanName | None:
        if value is None:
            return None
        return ClanName(value)
