from src.services.inventory_control import InventoryMapping
from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest

@pytest.fixture
def inventory_mapping():
    # Using a smaller, controlled inventory for tests
    return InventoryMapping("data/inventory_base_data.csv")

@pytest.fixture
def sample_recipe():
    # Create a dish and add ingredients to its recipe
    dish = Dish("pizza", 30.00)
    dish.add_ingredient_dependency(Ingredient("queijo mussarela"), 5)
    dish.add_ingredient_dependency(Ingredient("tomate"), 2)
    return dish.recipe

@pytest.fixture
def unavailable_recipe():
    # Create a dish and add ingredients to its recipe
    dish = Dish("pizza_grande", 50.00)
    dish.add_ingredient_dependency(Ingredient("queijo mussarela"), 500) # Amount unavailable in inventory
    dish.add_ingredient_dependency(Ingredient("tomate"), 2)
    return dish.recipe

def test_check_recipe_availability_when_available(inventory_mapping, sample_recipe):
    """ Test if a recipe is correctly identified as available """
    assert inventory_mapping.check_recipe_availability(sample_recipe) is True

def test_check_recipe_availability_when_unavailable(inventory_mapping, unavailable_recipe):
    """ Test if a recipe is correctly identified as unavailable """
    assert inventory_mapping.check_recipe_availability(unavailable_recipe) is False

def test_consume_recipe(inventory_mapping, sample_recipe):
    """ Test if consuming a recipe correctly updates the inventory """
    initial_queijo_amount = inventory_mapping.inventory.get(Ingredient("queijo mussarela"), 0)
    initial_tomate_amount = inventory_mapping.inventory.get(Ingredient("tomate"), 0)

    inventory_mapping.consume_recipe(sample_recipe)

    assert inventory_mapping.inventory[Ingredient("queijo mussarela")] == initial_queijo_amount - 5
    assert inventory_mapping.inventory[Ingredient("tomate")] == initial_tomate_amount - 2

def test_consume_unavailable_recipe_raises_error(inventory_mapping, unavailable_recipe):
    """ Test if trying to consume an unavailable recipe raises a ValueError """
    with pytest.raises(ValueError):
        inventory_mapping.consume_recipe(unavailable_recipe)