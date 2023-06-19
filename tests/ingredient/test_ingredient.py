from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_vegan = Ingredient('tomate')
    ingredient_animal_derived = Ingredient('presunto')
    ingredient_invalid = Ingredient('')

    assert ingredient_vegan == ingredient_vegan
    assert ingredient_vegan != ingredient_animal_derived
    assert ingredient_invalid.name == ''

    assert ingredient_vegan.restrictions == set()

    assert ingredient_vegan.__hash__() == ingredient_vegan.__hash__()
    assert ingredient_vegan.__hash__() != ingredient_animal_derived.__hash__()

    assert ingredient_vegan.__repr__() == "Ingredient('tomate')"
