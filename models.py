from pydantic import BaseModel, Field
from typing import List
import datetime

class Item(BaseModel):
    """
    Defines the structure of an item listed in a receipt.
    """
    shortDescription: str = Field(..., pattern=r"^[\w\s\-]+$")
    price: str = Field(..., pattern=r"^\d+\.\d{2}$")

class Receipt(BaseModel):
    """
    Defines the structure and validation rules for a receipt.
    """
    retailer: str = Field(..., pattern=r"^[\w\s\-&]+$")
    purchaseDate: datetime.date
    purchaseTime: datetime.time
    items: List[Item] = Field(..., min_items=1)
    total: str = Field(..., pattern=r"^\d+\.\d{2}$")
