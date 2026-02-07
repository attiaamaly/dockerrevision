import random
from fastapi import FastAPI

#API endpoint defined 

#home page : If you go to /, you see a welcome message
@app.get("/")
def home():
    return {"message": "Welcome to the Randomizer API"}

#URL example: /random/10
#max_value is a number from the URL
#Returns a random number between 1 and max_value
@app.get("/random/{max_value}")
def get_random_number(max_value: int):
    return {
        "max": max_value,
        "random_number": random.randint(1, max_value)
    }

