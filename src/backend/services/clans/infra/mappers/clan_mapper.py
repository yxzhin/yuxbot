from ...domain.entities import Clan
from ..models import ClanModel


class ClanMapper:
    @staticmethod
    def to_domain(model: ClanModel | None) -> Clan | None:
        if model is None:
            return None

        clan = Clan(
            clan_id=model.clan_id,
            clan_name=model.clan_name,
            clan_tag=model.clan_tag,
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
            clan_name=clan.clan_name,
            clan_tag=clan.clan_tag,
            owner_id=clan.owner_id,
            created_at=clan.created_at,
        )
        return model
