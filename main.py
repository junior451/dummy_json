from fastapi import FastAPI
import requests

app = FastAPI()

response = requests.get('https://dummyjson.com/users?limit=0')
data = response.json()['users'] #get users key from the dict object

@app.get("/users")
def read_users(firstName: str = None, lastName: str = None):
  new_users = []

  for user in data:
    if firstName and user["firstName"] != firstName:
      continue
    if lastName and user["lastName"] != lastName:
      continue
    new_users.append({"id": user["id"], "firstName": user["firstName"], "lastName":user["lastName"], "email": user["email"], "phone": user["phone"]})

  new_response = {"total":len(data), "count":len(new_users), "users": new_users} 

  return new_response