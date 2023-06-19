from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    vegan_ingredient = Ingredient('tomate')
    ingredient_animal_derived = Ingredient('presunto')
    invalid_ingredient = Ingredient('')

    assert vegan_ingredient == vegan_ingredient
    assert vegan_ingredient != ingredient_animal_derived
    assert invalid_ingredient.name == ''

    assert vegan_ingredient.restrictions == set()

    assert vegan_ingredient.__hash__() == vegan_ingredient.__hash__()
    assert vegan_ingredient.__hash__() != ingredient_animal_derived.__hash__()

    assert vegan_ingredient.__repr__() == "Ingredient('tomate')"
