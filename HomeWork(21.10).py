import json
import requests

url = "https://jsonplaceholder.typicode.com/todos"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)

for x in data:
    print(f"ID: {x['id']}")
    print(f"Title: {x['title']}")
    print(f"Completed: {x['completed']}")
    print()

print(response.text)