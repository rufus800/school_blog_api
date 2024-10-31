# School Blog API

This is a simple school blog API built with FastAPI, MongoDB (using Motor), and Pydantic for data validation.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/school_blog_api.git
    cd school_blog_api
    ```

2. Create a virtual environment and install the dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    uvicorn app.main:app --reload
    ```

4. Access the API at `http://127.0.0.1:8000`.

## Endpoints

- **Create Blog**: `POST /blogs/`
- **Read Blogs**: `GET /blogs/`
- **Read Blog**: `GET /blogs/{blog_id}`
- **Update Blog**: `PUT /blogs/{blog_id}`
- **Delete Blog**: `DELETE /blogs/{blog_id}`
