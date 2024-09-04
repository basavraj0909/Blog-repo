import requests

#TODO 1. Create a New User (POST /users/)
# url = 'http://localhost:8000/users/'
# headers = {
#     "Authorization" : "Bearer <your_token>"
# }
# data= {
#     "first_name": "Alice3",
#     "last_name": "Johnso3",
#     "age": 18,
#     "email": "alice3@example.com",
#     "mobile_number": "9881167673"
# }
# response = requests.post(url,headers=headers, json=data)


###TODO 2. Get All Users (GET /users/)
url = 'http://localhost:8000/users/'
headers = {"Authorization" : "Bearer <your_token>"}
params = {'page': 2}
response = requests.get(url, headers=headers, params=params)
print(type(response.c))


#TODO 3. **Get a Single User (GET /users/<int:pk>/)**
# url = "http://localhost:8000/users/1/"
# headers = {"Authorization": "Bearer <your_token>"}
# response = requests.get(url, headers=headers)


#TODO 4. **Update a User (PUT /users/<int:pk>/)**
# url = "http://localhost:8000/users/1/"
# headers = {"Authorization": "Bearer <your_token>"}
# data = {
#     "first_name": "Alice",
#     "last_name": "Updated Johnson",
#     "age": 29,  # Updated age
#     "email": "alice.johnson@example.com",
#     "mobile_number": "1122334455"
# }
# response = requests.put(url, headers=headers, json=data)


#TODO 6. **Delete a User (DELETE /users/<int:pk>/)**
# url = "http://localhost:8000/users/1/"
# headers = {"Authorization": "Bearer <your_token>"}
# response = requests.delete(url, headers=headers)



print("Status Code:", response.status_code)
print("Response JSON:", response.json())