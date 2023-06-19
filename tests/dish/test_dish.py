from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish_lasanha = Dish('lasanha', 28.99)
    dish_empada = Dish('empada', 8.99)
    dish_invalid = Dish('')

    assert dish_lasanha == dish_lasanha
    assert dish_lasanha != dish_empada
    assert dish_invalid.name == ''

    assert dish_empada.__repr__() == "Dish('empada', R$8,99)"

    assert dish_empada.__hash__() == dish_empada.__hash__()
    assert dish_empada.__hash__() != dish_lasanha.__hash__()

    dish_lasanha.add_ingredient_dependency(Ingredient('macarrão'), 500)
    dish_lasanha.add_ingredient_dependency(Ingredient('queijo'), 250)
    dish_lasanha.add_ingredient_dependency(Ingredient('presunto'), 250)
    dish_lasanha.add_ingredient_dependency(Ingredient('molho de tomate'), 1)
    dish_lasanha.add_ingredient_dependency(Ingredient('carne moída'), 400)

    assert dish_lasanha.get_ingredients() == set([
        Ingredient('macarrão'),
        Ingredient('queijo'),
        Ingredient('presunto'),
        Ingredient('molho de tomate'),
        Ingredient('carne moída'),
        ])

    assert dish_lasanha.get_restrictions() != set('')

    with pytest.raises(TypeError):
        Dish('lasanha', 'R$20,99')

    with pytest.raises(TypeError):
        Dish('lasanha', '-20,99')
