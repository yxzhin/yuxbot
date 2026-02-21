class ClansDomainError(Exception):
    pass


class InvalidClanNameLengthError(ClansDomainError):
    pass


class InvalidClanTagLengthError(ClansDomainError):
    pass


class InvalidClanTagValueError(ClansDomainError):
    pass


class ClanAlreadyExistsError(ClansDomainError):
    pass


class ClanNotFoundError(ClansDomainError):
    pass


class ClanFullError(ClansDomainError):
    pass


class PlayerAlreadyInClanError(ClansDomainError):
    pass
