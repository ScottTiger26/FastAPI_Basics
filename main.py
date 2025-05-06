from fastapi import FastAPI

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

@app.get("/items")
async def list_items():
    return {"message": "list_items_route"}

@app.get("/items/{item_id}")
async def get_item(item_id):
    return {"item_id": item_id}