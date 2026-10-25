# Dummy JSON Filtered Users API


## Brief explanation of my approach
I used a catch-try block to handle exceptions when making the request to the upstream API. To return all data from the API, I set the limit query parameter to 0 and then set the the users array to the data variable.

The read_users() function handles the request for the '/users' path. The function takes firstName and lastName as query Parameters with the default set to none for each parameter. I filtered the json response by not appending the user to the users array if firstName or lastName is passed in the query string but they dont match the user's firstName or lastName in the iteration. The new json response is then returned as the new structure with the total, count and users values.



## Assumptions
For testing purposes, The data will not change and the response will always be returned in the same structure and order

## How to run and test the app

### Requirements
- Python 3.9+
- pip

### Clone the repository
```bash
  git clone https://github.com
  cd project-name
```

### Install dependencies
```bash
pip install fastapi uvicorn httpx pytest
```

### Run the application:
```bash
  uvicorn main:app --reload                                                         
```

### Test the application
```bash
  pytest . -v 
```

