from fastapi import FastAPI
from pydantic import BaseModel
from calc import calculate
app = FastAPI(title = "My Calculator")

class User_input(BaseModel):
    x:int
    y:int
    options:str


@app.post("/calculate")
def calculatee(input:User_input):
    print(input)
    return calculate(input.x,input.y,input.options)
