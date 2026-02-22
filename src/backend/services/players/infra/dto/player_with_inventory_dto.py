from ...domain.entities import InventoryItem, Player


class PlayerWithInventoryDTO:
    def __init__(self, player: Player, inventory: list[InventoryItem]):
        self.player = player
        self.inventory = inventory
