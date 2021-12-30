
from pydantic import BaseModel as Schema, Field
from typing import List

class UserSchema(Schema):
    """A User object"""
    id : int
    username : str
    firstName : str
    lastName : str
    email : str
    password : str
    phone : str
    userStatus : int

    @classmethod
    def example(cls):
        return cls(
            id=10,
            username="theUser",
            firstName="John",
            lastName="James",
            email="john@email.com",
            password="12345",
            phone="12345",
            userStatus=4
        )

class UserListSchema(Schema):
    """Array of User objects"""
    __root__ : List[UserSchema]

class LoginRequestSchema(Schema):
    username : str
    password : str = Field(description="The password for login in clear text")

class UsernameSchema(Schema):
    username : str = Field(
        description="The username of the User that needs to be fetched.", 
        required=True
    )

class UserErrorSchema(Schema):
    msg : List[str]

    @classmethod
    def example(cls):
        return cls(
            msg=["A User error message here."]
        )

class LoginSuccessSchema(Schema):

    __root__ : str

    class Config:
        headers = {
            "X-Rate-Limit":{
                "description":"calls per hour allowed by the user",
                "type":"integer",
                "schema":{
                    "type":"integer"
                }
            },
            "X-Expires-After":{
                "description":"date in UTC when token expires",
                "type":"string",
                "schema":{
                    "type":"strings"
                }
            }
        }

class LoginErrorSchema(Schema):
    
    details : str 

    @classmethod
    def example(cls):
        return cls(details="Invalid username/password supplied")

class LogoutSuccessSchema(Schema):
    __root__ : str 
    