from sqlalchemy.types import STRINGTYPE, TypeDecorator

from ...domain.value_objects import ClanTag


class ClanTagMapper(TypeDecorator):
    impl = STRINGTYPE

    def process_bind_param(self, clan_tag: ClanTag | None, dialect) -> str | None:
        if clan_tag is None:
            return None
        return clan_tag.value

    def process_result_value(self, value: str | None, dialect) -> ClanTag | None:
        if value is None:
            return None
        return ClanTag(value)
