from src.services.menu_data import MenuData
from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest

@pytest.fixture
def menu_data():
    return MenuData("data/menu_base_data.csv")

def test_menu_data_initialization(menu_data):
    assert len(menu_data.dishes) > 0

    # Test a specific dish to see if it and its ingredients were loaded correctly
    lasanha = Dish('lasanha presunto', 25.90)
    found_dish = None
    for dish in menu_data.dishes:
        if dish == lasanha:
            found_dish = dish
            break
    
    assert found_dish is not None
    
    expected_ingredients = {
        Ingredient('queijo mussarela'),
        Ingredient('tomate'),
        Ingredient('farinha de trigo'),
        Ingredient('sal'),
        Ingredient('água'),
        Ingredient('presunto'),
    }
    assert found_dish.get_ingredients() == expected_ingredients