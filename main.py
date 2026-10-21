from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/users")
def read_users():
  response = requests.get('https://dummyjson.com/users?limit=0')
  data = response.json()
  data = data['users']

  new_users = []

  for user in data:
    new_users.append({"id": user["id"], "firstName": user["firstName"], "lastName":user["lastName"], "email": user["email"], "phone": user["phone"]})

  new_response = {"total":len(data), "count":len(new_users), "users": new_users} 

  return new_response