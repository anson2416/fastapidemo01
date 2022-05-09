from typing import Optional
from pydantic import BaseModel, Field


class Item(BaseModel):
    """Perform validations of the resources '/item/{id}'"""
    name: str = Field(None, 
                        title="Example title...", 
                        min_length=3,
                        max_length=10)
    price: float = Field(None, title ='Price 300')
    is_offer: Optional[bool] = Field(False, title='Is offer')