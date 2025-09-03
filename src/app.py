from fastapi import FastAPI, HTTPException, Query, status

from src.models.ingredient import Restriction
from src.services.menu_builder import MenuBuilder
from src.services.menu_data import MenuData
from src.services.inventory_control import InventoryMapping

app = FastAPI(title="Restaurante Chapa Quente")
menu_builder = MenuBuilder(
    MenuData("data/menu_base_data.csv"),
    InventoryMapping("data/inventory_base_data.csv"),
)


restriction_options = {k: {"value": k} for k in Restriction._member_names_}


@app.get("/", tags=["menu"])
def get_menu(
    restriction: str = Query(default="", examples=restriction_options)
):
    return menu_builder.get_main_menu(
        restriction=Restriction._member_map_.get(restriction)
    )


@app.post("/order", tags=["menu"], status_code=status.HTTP_201_CREATED)
def make_dish_order(dish_name: str):
    try:
        menu_builder.make_order(dish_name)
    except ValueError as err:
        if str(err) == "Dish does not exist":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(err),
            )
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Dish can't be prepared due to missing ingredients",
        )