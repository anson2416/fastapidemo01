from fastapi import FastAPI
from .items import item_router

app = FastAPI()

app.include_router(item_router)

@app.get("/")
def root():
    return "ok"

# @app.get("/item/{id}")    
# def read_item(id: int):
#     return id

