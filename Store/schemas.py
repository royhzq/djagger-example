
from pydantic import BaseModel as Schema, Field
from typing import List
from enum import Enum

class Status(str, Enum):
    available = 'available'
    pending = 'pending'
    sold = 'sold'

class Category(Schema):
    """Toy Category"""
    id : int
    name : str

class Tag(Schema):
    """Toy Tag"""
    id : int
    name : str

class Toy(Schema):
    """Toy Schema"""
    id : int 
    category : Category
    photoUrls : List[str]
    tags : List[Tag]
    status : Status = Status.available
