"""Requests in Python"""

import requests

URL = "https://jsonplaceholder.typicode.com/users"

# get method
r = requests.get(URL, timeout=10)

r = r.json()

for user in r:
    print(user["name"])

# post method
user = {
    "name": "Santiago"
}

r2 = requests.post(URL, timeout=10, data=user)
print(r2.status_code)

# If the API is protected, we need the header including the API key
APIKEY = "12345"
header = {
    "Authorization": f"Bearer {APIKEY}"
}

r3 = requests.delete(URL, timeout=10, headers=header)
