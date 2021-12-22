from pydantic import BaseModel as Schema, Field
from typing import List, Optional
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

class ToySchema(Schema):
    """Toy Schema"""
    id : Optional[int]
    name : str
    category : Optional[Category]
    photoUrls : List[str]
    tags : Optional[List[Tag]]
    status : Optional[Status] = Status.available

    @classmethod
    def example(cls):
        return cls(
            id=10,
            name="doggie",
            category=Category(id=1, name="Dogs"),
            photoUrls=["string"],
            tags=[Tag(id=0, name="string")],
            status="available"
        )

class ToyArraySchema(Schema):
    """An array of Toys""" 
    __root__: List[ToySchema]

class InvalidToySchema(Schema):
    """Validation Error"""
    message : List[str]

class ToyNotFoundSchema(Schema):
    """Not Found Error"""
    message : List[str] 

class StatusSchema(Schema):
    status : Status = Field(
        default="available", 
        description="Enum of status", 
        enum=["available", "pending", "sold"]
    )

class TagQueryParamSchema(Schema):
    """Tags to filter by"""
    tags : List[str] = Field(description="Relevant tags", example=["Dog", "Cat"])

class ToyIdSchema(Schema):
    """Path parameters for Toy Id"""
    toyId : int = Field(description="ID of Toy to return")

class ToyIdFormSchema(Schema):
    """Form parameters in request body to query a single Toy"""
    toyId : int = Field(description="ID of Toy that needs to be updated")
    name : Optional[str] = Field(description="Name of Toy to update")
    status : Optional[str] = Field(description="Status of Toy to update")

class ToyDeleteHeaderSchema(Schema):
    api_key : str

class ToyMetaDataSchema(Schema):
    additionalMetadata : str

class ToyUploadImageSchema(Schema):
    """Example values are not available for application/octet-stream media types."""
    ...
    __root__ : bytes

class ToyUploadImageSuccessSchema(Schema):
    """Successful operation for image uploading"""
    code : int
    type_ : str = Field(alias="type") # 'type' is a reserved keyword in Python. So we alias it to represent it correctly in the docs.
    message :str