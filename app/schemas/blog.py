from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class BlogBase(BaseModel):
    title: str
    content: str
    author: str

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BlogBase):
    pass

class BlogInDB(BlogBase):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
