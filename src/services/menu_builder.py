from typing import Dict, List

from src.services.inventory_control import InventoryMapping
from src.services.menu_data import MenuData

Inventory = Dict[str, int]
Menu = List[Dict[str, object]]


class MenuBuilder:
    def __init__(self, menu_data: MenuData, inventory: InventoryMapping):
        self.menu = menu_data
        self.inventory = inventory

    def get_main_menu(self, restriction: str = None) -> List[Dict[str, object]]:
        menu = []
        for dish in self.menu.dishes:
            if self.inventory.check_recipe_availability(dish.recipe):
                if restriction is None or restriction not in dish.get_restrictions():
                    menu.append(
                        {
                            'dish_name': dish.name,
                            'ingredients': list(dish.get_ingredients()),
                            'price': dish.price,
                            'restrictions': list(dish.get_restrictions()),
                        }
                    )

        return menu