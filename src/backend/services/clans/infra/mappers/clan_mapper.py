from ...domain.entities import Clan
from ...domain.value_objects import ClanName, ClanTag
from ..dto import ClanDTO
from ..models import ClanModel


class ClanMapper:
    @staticmethod
    def to_domain(model: ClanModel | None) -> Clan | None:
        if model is None:
            return None

        clan = Clan(
            clan_id=model.clan_id,
            clan_name=ClanName(model.clan_name),
            clan_tag=ClanTag(model.clan_tag),
            owner_id=model.owner_id,
            created_at=model.created_at,
        )
        return clan

    @staticmethod
    def to_orm(clan: Clan | None) -> ClanModel | None:
        if clan is None:
            return None

        model = ClanModel(
            clan_id=clan.clan_id,
            clan_name=clan.clan_name.value,
            clan_tag=clan.clan_tag.value,
            owner_id=clan.owner_id,
            created_at=clan.created_at,
        )
        return model

    @staticmethod
    def to_dto(clan: Clan | None) -> ClanDTO | None:
        if clan is None:
            return None

        dto = ClanDTO(
            clan_id=clan.clan_id,
            clan_name=clan.clan_name.value,
            clan_tag=clan.clan_tag.value,
            owner_id=clan.owner_id,
            created_at=clan.created_at,
        )
        return dto
