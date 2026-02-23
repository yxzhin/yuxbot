class PlayersDomainError(Exception):
    pass


class InsufficientAmountError(PlayersDomainError):
    pass


class PlayerAlreadyExistsError(PlayersDomainError):
    pass


class PlayerNotFoundError(PlayersDomainError):
    pass


class ItemAlreadyExistsError(PlayersDomainError):
    pass


class ItemNotFoundError(PlayersDomainError):
    pass
