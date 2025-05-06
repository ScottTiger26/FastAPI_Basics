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
