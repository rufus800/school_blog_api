import os

MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "school_blog")
