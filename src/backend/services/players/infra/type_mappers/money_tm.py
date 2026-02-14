from sqlalchemy.types import INTEGER, TypeDecorator

from ...domain.value_objects import Money


class MoneyTypeMapper(TypeDecorator):
    impl = INTEGER

    def process_bind_param(self, money: Money | None, dialect) -> int | None:
        if money is None:
            return None
        return money.amount

    def process_result_value(self, amount: int | None, dialect) -> Money | None:
        if amount is None:
            return None
        return Money(amount)
