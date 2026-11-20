import requests
from pprint import pprint

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()
for user in data:
    print(f"Usuarios: {user['id']} - {user['name']}")