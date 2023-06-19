import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, encoding='utf8', newline='') as file:
            reader_data = csv.DictReader(file)

            for row in reader_data:
                dish_name = row['dish']
                dish_price = float(row['price'])
                dish_ingredient = row['ingredient']
                dish_recipe_amount = int(row['recipe_amount'])

                self.dishes.add(Dish(dish_name, dish_price))

                dish_next = next(iter(self.dishes))

                dish_next.add_ingredient_dependency(
                    Ingredient(dish_ingredient),
                    dish_recipe_amount)
