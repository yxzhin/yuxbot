class PlayersDomainError(Exception):
    pass


class InsufficientBalanceError(PlayersDomainError):
    pass


class PlayerAlreadyExistsError(PlayersDomainError):
    pass


class PlayerNotFoundError(PlayersDomainError):
    pass
