from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/users")
def read_users():
  response = requests.get('https://dummyjson.com/users?limit=0')
  data = response.json()

  return data