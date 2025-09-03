from src.services.menu_builder import MenuBuilder
from src.models.ingredient import Restriction
import pytest


@pytest.fixture
def menu_builder():
    return MenuBuilder()


def test_menu_builder_initialization(menu_builder):
    """Test if the menu builder is initialized with the correct data"""
    assert len(menu_builder.menu_data.dishes) > 0


def test_get_main_menu(menu_builder):
    """Test if the main menu is built correctly"""
    main_menu = menu_builder.get_main_menu()

    # All dishes from menu_base_data should be available
    assert len(main_menu) == 2

    # Test with a restriction
    main_menu_no_lactose = menu_builder.get_main_menu(
        restriction=Restriction.LACTOSE
    )
    assert len(main_menu_no_lactose) == 0

    # Find 'lasanha presunto' to consume its ingredients
    lasanha_presunto = None
    for dish in menu_builder.menu_data.dishes:
        if dish.name == "lasanha presunto":
            lasanha_presunto = dish
            break

    # Consume 'presunto' until it's not enough for another 'lasanha presunto'
    # Initial presunto is 50, recipe needs 15. After 3 consumptions, 5 left.
    for _ in range(3):
        menu_builder.inventory.consume_recipe(lasanha_presunto.recipe)

    main_menu_depleted = menu_builder.get_main_menu()

    # 'lasanha presunto' should be unavailable, 'lasanha berinjela' should be
    assert len(main_menu_depleted) == 1
    dish_names_in_menu = {d["dish_name"] for d in main_menu_depleted}
    assert "lasanha presunto" not in dish_names_in_menu
    assert "lasanha berinjela" in dish_names_in_menu