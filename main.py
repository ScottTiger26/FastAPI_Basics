<<<<<<< HEAD
from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()

#
# @app.get("/")
# async def read_root():
#     return {"message": "Hello Vishwajeet"}
#
#
# # If path parameter is not provided then the parameter inside the function is treated as query parameter
# @app.get("/greet")
# async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
#     return {"message": f"Hello {name}, Hope your are fantastic!!!!  :)))), ", "age": age}
#
#
# class BookCreateModal(BaseModel):
#     title: str
#     author: str
#
#
# @app.post("/create_book")
# async def create_book(book_data: BookCreateModal):
#     return {
#         "title": book_data.title,
#         "author": book_data.author
#     }
#
#
# @app.get('/get_headers', status_code=200)
# # @app.get('/get_headers', status_code=500)  # We can customize the status code from here.
# async def get_headers(
#         accept: str = Header(None),
#         content_type: str = Header(None),
#         user_agent: str = Header(None),
#         host: str = Header(None),
# ):
#     request_header = {}
#     request_header["Accept"] = accept
#     request_header["Content-Type"] = content_type
#     request_header["User-Agent"] = user_agent
#     request_header["Host"] = host
#     return request_header


# ********************************************** CRUD *************************************
books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downy",
        "publisher": "O'Reilly Media",
        "published_date": "2020-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Think Different",
        "author": "Allen V. Downy",
        "publisher": "O'Reilly Media",
        "published_date": "2020-01-01",
        "page_count": 1144,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Python Vibes",
        "author": "Rodriguez B. Downy",
        "publisher": "Tata MacGraw Hill",
        "published_date": "2025-01-01",
        "page_count": 1342,
        "language": "Sanskrit",
    }
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
# Model to Update
class BookUpdate(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

# CRUD Routing
@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books

@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump() # It converts the new_book to dictionary
    books.append(new_book)
    return new_book

@app.get("/books/{book_id}")
async def get_a_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= "Book not Found"
    )

@app.patch("/books/{book_id}")
async def update_a_book(book_id: int, book_update_data: BookUpdate) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language

            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Does not exist."
    )

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

        return {}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Book not found"
    )
=======
#
#
# @app.get("/")
# async def root():
#     return {"message": "hello world"}
#
#
# @app.post("/")
# async def post():
#     return {"message": "hello from the post route"}
#
#
# @app.put("/")
# async def put():
#     return {"message": "hello from the put route"}
#
#
# @app.get("/users")
# async def list_users():
#     return {"message": "list users route"}
#
#
# @app.get("/users/me")
# async def get_current_user():
#     return {"Message": "this is the current user"}
#
#
# @app.get("/users/{user_id}")
# async def get_user(user_id: str):
#     return {"user_id": user_id}
#
#
# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"
#
#
# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {"food_name": food_name, "message": "you are healthy"}
#
#     if food_name.value == "fruits":
#         return {
#             "food_name": food_name,
#             "message": "you are still healthy, but like sweet things",
#         }
#     return {"food_name": food_name, "message": "i like chocolate milk"}
#
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# @app.get("/old_items")
# async def list_old_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]
#
#
# @app.get("/items/{item_id}")
# async def get_item(
#     item_id: str, sample_query_param: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "sample_query_param": sample_query_param}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consectetur."
#             }
#         )
#     return item
#
#
# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consectetur."
#             }
#         )
#         return item
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
#
#
# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result
#
# # To be able to pass multiple queries
# # q: list[str]     <------- Changed
# #     | None = Query(
# #         None,
# #         min_length=3,
# #         max_length=10,
# #         title="Sample query string",
# #         description="This is a sample query string.",
# #         alias="item-query",
# #     )
#
# # To set the default value without None
# # q: str
# #     | None = Query(
# #         ...,          <------- Changed
# #         min_length=3,
# #         max_length=10,
# #         title="Sample query string",
# #         description="This is a sample query string.",
# #         alias="item-query",
# #     )
# @app.get("/items")
# async def read_items(
#     q: str
#     | None = Query(
#         None,
#         min_length=3,
#         max_length=10,
#         title="Sample query string",
#         description="This is a sample query string.",
#         alias="item-query",
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
#
# @app.get("/items_hidden")
# async def hidden_query_route(
#     hidden_query: str | None = Query(None, include_in_schema=False)
# ):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {"hidden_query": "Not found"}
#
#
# @app.get("/items_validation/{item_id}")
# # async def read_items_validation(item_id: int = Path(..., title="THe ID of the item to get", ge=10), q: str | None = Query(None, alias='item_query')):
# async def read_items_validation(
#         item_id: int = Path(..., title="THe ID of the item to get", ge=10, le=100),
#         q: str = "hello",
#         size: float = Query(..., gt=0, lte=7.75)
#             ):
#     results = {"item_id": item_id, "size": size}
#     if q:
#         results.update({"q":q})
#     return results

from enum import Enum
from fastapi import Body, FastAPI, Query, Path
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


# Part-7 - Body Multiple parameters
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(
#         *,
#         item_id: int = Path(..., title="The ID of the item to get", ge=10),
#         q: str | None = None,
#         item: Item = Body(..., embed=True),
#         user: User,
#         importance: int = Body(..., embed=True)
# ):
#     results = {"item_id": item_id}
#
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     if importance:
#         results.update({"importance": importance})
#     return results

## Part 8 -> Body - Fields
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         None, title="The description of the item", max_length=300
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero.")
#     tax: float | None = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results

## Part 9 -> Body - Nested Models

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = []
    image: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/offers")
async def create_offer(offer: Offer = Body(..., embed=True)):
    return offer

@app.post("/image/multiple")
async def create_multiple_images(images: list[Image]):
    return images

@app.post("/blah")
async def create_some_blahs(blahs: dict[int, float]):
    return blahs
>>>>>>> 0ffc3bebdd122ffad77809bb7ca337fea56bf102
