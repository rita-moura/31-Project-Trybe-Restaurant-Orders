from src.services.menu_builder import MenuBuilder
from src.services.inventory_control import InventoryMapping
from src.services.menu_data import MenuData
import pytest

@pytest.fixture
def menu_builder():
    return MenuBuilder(
        menu_data=MenuData("data/menu_base_data.csv"),
        inventory=InventoryMapping("data/inventory_base_data.csv")
    )

def test_menu_builder_initialization(menu_builder):
    """ Test if the menu builder is initialized with the correct data """
    assert len(menu_builder.menu.dishes) > 0

def test_get_main_menu(menu_builder):
    """ Test if the main menu is built correctly """
    main_menu = menu_builder.get_main_menu()
    
    # All dishes from menu_base_data should be available with inventory_base_data
    assert len(main_menu) == len(menu_builder.menu.dishes)

    # Test with a depleted inventory
    depleted_inventory = InventoryMapping("data/inventory_base_data.csv")
    # Deplete an ingredient needed for 'lasanha'
    for ingredient in depleted_inventory.inventory:
        if ingredient.name == 'queijo presunto':
            depleted_inventory.inventory[ingredient] = 0
            break

    menu_builder_depleted = MenuBuilder(
        menu_data=MenuData("data/menu_base_data.csv"),
        inventory=depleted_inventory
    )
    main_menu_depleted = menu_builder_depleted.get_main_menu()
    
    assert len(main_menu_depleted) < len(menu_builder.menu.dishes)
    
    # Check that 'lasanha' is not in the depleted menu
    lasanha_in_menu = any(d['name'] == 'lasanha' for d in main_menu_depleted)
    assert not lasanha_in_menu