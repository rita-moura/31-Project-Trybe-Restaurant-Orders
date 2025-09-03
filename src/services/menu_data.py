import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        dishes_map = {}

        with open(source_path, encoding='utf8', newline='') as file:
            reader_data = csv.DictReader(file)

            for row in reader_data:
                dish_name = row['dish']
                dish_price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                # Encontra o prato existente ou cria um novo
                dish = dishes_map.get(dish_name)
                if dish is None:
                    dish = Dish(dish_name, dish_price)
                    dishes_map[dish_name] = dish
                    self.dishes.add(dish)

                # Adiciona o ingrediente ao prato correto
                dish.add_ingredient_dependency(
                    Ingredient(ingredient_name),
                    recipe_amount
                )