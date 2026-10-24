from fastapi import FastAPI
import requests

app = FastAPI()

try:
  response = requests.get('https://dummyjson.com/users?limit=0', timeout=5)
  response.raise_for_status()  # Raise an error for bad responses
  data = response.json()['users'] #get users key from the dict object

except requests.exceptions.RequestException as e:
  print(f"Something went wrong: {e}")
  data = []  # Fallback to an empty list if the request fails

@app.get("/users")
def read_users(firstName: str = None, lastName: str = None):
  new_users = []

  for user in data:
    if firstName and user["firstName"].lower() != firstName.lower():
      continue
    if lastName and user["lastName"].lower() != lastName.lower():
      continue
    new_users.append({"id": user["id"], "firstName": user["firstName"], "lastName":user["lastName"], "email": user["email"], "phone": user["phone"]})

  new_response = {"total":len(data), "count":len(new_users), "users": new_users} 

  return new_response