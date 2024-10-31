from fastapi import FastAPI
from app.database import connect_to_mongo, close_mongo_connection
from app.routers import blog

app = FastAPI()

app.include_router(blog.router)

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()
