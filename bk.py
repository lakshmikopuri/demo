from fastapi import FastAPI

app= FastAPI()
boook=[{"author_one":"author","catagory":"cat","sub":"maths"},
       {"author_one":"author","catagory":"cat","sub":"maths"},
       {"author_one":"author","catagory":"cat","sub":"maths"}]
@app.get("/books")
async def read_all_books():
    return boook
