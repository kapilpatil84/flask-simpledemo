import requests

response = requests.get("http://localhost:5000/")
print(response.text)

response = requests.get("http://localhost:5000/login")
print(response.text)

response = requests.get("http://localhost:5000/login/")
print(response.text)

response = requests.get("http://localhost:5000/profile")
print(response.text)