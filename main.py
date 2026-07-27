from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello from fastapi"}


@app.get("/sum")
def add_numbers(a: int, b: int):
    return {"result": a + b}