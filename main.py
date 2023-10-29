from fastapi import FastAPI

app = FastAPI()

# Print "Hello World"
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Path parameters
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}