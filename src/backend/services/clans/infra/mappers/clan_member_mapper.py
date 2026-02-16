from ...domain.entities import ClanMember
from ..dto import ClanMemberDTO
from ..models import ClanMemberModel


class ClanMemberMapper:
    @staticmethod
    def to_domain(model: ClanMemberModel | None) -> ClanMember | None:
        if model is None:
            return None

        clan_member = ClanMember(
            clan_member_id=model.clan_member_id,
            player_id=model.player_id,
            clan_id=model.clan_id,
            joined_at=model.joined_at,
        )
        return clan_member

    @staticmethod
    def to_orm(clan_member: ClanMember | None) -> ClanMemberModel | None:
        if clan_member is None:
            return None

        model = ClanMemberModel(
            clan_member_id=clan_member.clan_member_id,
            player_id=clan_member.player_id,
            clan_id=clan_member.clan_id,
            joined_at=clan_member.joined_at,
        )
        return model

    @staticmethod
    def to_dto(clan_member: ClanMember | None) -> ClanMemberDTO | None:
        if clan_member is None:
            return None

        dto = ClanMemberDTO(
            clan_member_id=clan_member.clan_member_id,
            player_id=clan_member.player_id,
            clan_id=clan_member.clan_id,
            joined_at=clan_member.joined_at,
        )
        return dto
