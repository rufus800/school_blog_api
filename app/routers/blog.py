from fastapi import APIRouter, HTTPException
from app.models.blog import BlogCreate, BlogUpdate, BlogInDB
from app.database import database
from bson import ObjectId
from typing import List

router = APIRouter()

@router.post("/blogs/", response_model=BlogInDB)
async def create_blog(blog: BlogCreate):
    blog_dict = blog.dict()
    result = await database["blogs"].insert_one(blog_dict)
    created_blog = await database["blogs"].find_one({"_id": result.inserted_id})
    return created_blog

@router.get("/blogs/", response_model=List[BlogInDB])
async def read_blogs():
    blogs = await database["blogs"].find().to_list(1000)
    return blogs

@router.get("/blogs/{blog_id}", response_model=BlogInDB)
async def read_blog(blog_id: str):
    blog = await database["blogs"].find_one({"_id": ObjectId(blog_id)})
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@router.put("/blogs/{blog_id}", response_model=BlogInDB)
async def update_blog(blog_id: str, blog: BlogUpdate):
    blog_dict = blog.dict()
    result = await database["blogs"].update_one({"_id": ObjectId(blog_id)}, {"$set": blog_dict})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    updated_blog = await database["blogs"].find_one({"_id": ObjectId(blog_id)})
    return updated_blog

@router.delete("/blogs/{blog_id}")
async def delete_blog(blog_id: str):
    result = await database["blogs"].delete_one({"_id": ObjectId(blog_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"detail": "Blog deleted"}
