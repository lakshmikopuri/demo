from fastapi import FastAPI

app= FastAPI()
books=[
    {"title":"title_one","author":"author_one","catagory":"sicence"},
    {"title": "title_two", "author": "author_two", "catagory": "sicence"},
    {"title": "title_three", "author": "author_three", "catagory": "maths"},
    {"title": "title_four", "author": "author_four", "catagory": "sicence"}
]
@app.get("/")
async def first_api():
    return {"messs"}

