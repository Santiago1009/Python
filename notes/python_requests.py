"""Requests in Python"""

import requests

URL = "https://jsonplaceholder.typicode.com/users"

# get method
r = requests.get(URL, timeout=10)

r = r.json()

for user in r:
    print(user["name"])

# post method
SECOND_URL = "https://jsonplaceholder.typicode.com/users"
user = {
    "name": "Santiago"
}

r2 = requests.post(SECOND_URL, timeout=10, data=user)
print(r2.status_code)
