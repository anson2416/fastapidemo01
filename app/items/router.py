from fastapi import APIRouter
from typing import List

from .schemas import ItemSchema

router = APIRouter()

items = []

@router.get("/items", tags=['items'], response_model=List[ItemSchema])
def list_items() -> List[ItemSchema]:
    # return []
    return items


# @router.get("/items/{id}", tags=['items'])    
# def read_item(id:int) -> int:
#     return id


@router.get("/items/name={name}", tags=['items'])    
def read_item(name:str) -> List[ItemSchema]:
    # print('--->', type(name), name) # str, not dict
    for item in items:
        # if item.name == name:
        print('--->', type(item), item)
        if item.name == name:
            return item
    
    return "No user found!"



@router.post("/items", tags=['items'], response_model=ItemSchema)
def create_item(data: ItemSchema):
    items.append(data)
    return data