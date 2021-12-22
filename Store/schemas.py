
from pydantic import BaseModel as Schema, Field
from typing import List, Dict
from enum import Enum
import datetime

class InventoryByStatusSchema(Schema):
    """A map of status codes to quantities"""
    __root__ : Dict[str, int]

class OrderStatus(str, Enum):
    placed = 'placed'
    approved = 'approved'
    delivered = 'delivered'

class OrderSchema(Schema):

    id : int
    toyId : int
    quantity : int
    shipDate : datetime.datetime
    status : OrderStatus
    complete : bool

class OrderIDSchema(Schema):
    
    orderId : int = Field(description="ID of order that needs to be fetched")

class InvalidInputSchema(Schema):
    """Invalid Input"""
    ...

class NotFoundSchema(Schema):
    """Invalid Input"""
    __root__ : str = Field("Not found")