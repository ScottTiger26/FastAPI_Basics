from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get("/", description="This is our base get rute")
async def Base_get_route():
    return {"message": "Hello World!!"}

@app.post("/")
async def post():
    return {"message": "Helo from post"}

@app.put("/")
async def put():
    return {"message": "Helo from put"}

@app.get("/users")
async def list_users():
    return {"message": "list_items_route"}

@app.get("/users/me")
async def get_current_user():
    return {"message": "This is the current user"}
@app.get("/users/{user_id}")
async def get_item(user_id: str):
    return {"user_id": user_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"message": "You are healthy"}
    if food_name.value == "fruits":
        return{
            "food name": food_name,
            "message": "You are still healthy but like sweet things"
        }
    return{
            "message": "I like chocolate milk"
    }

# Fake items databse
fake_items_db = [{"item_name": "foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items")
async def list_items(skip: int = 0,limit: int = 10):
    return fake_items_db[skip: skip+limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, sample_query_param: str, q: str | None,  short: bool= False):
    item = {"item_id": item_id, "sample_query_param": sample_query_param}
    if q:
        item.update({"q":q})
    if not short:
        item.update({
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consectetur."
        })
        return item

@app.get("/user/{user_id}/item/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {
                "description": "Lorem ipsum dolor sit them, consecutoe sjdlkjdsl elit, Ut consecutor"
            }
        )
        return item
