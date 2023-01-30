import requests

headers = {"Auth": "827e8e1a-119c-48e2-af1c-cef81f933a5a"}

for i in range(2000):
    response = requests.get(f"http://localhost:5000/offer-matches/{i}", headers=headers)
    print(f"Response json is {response.json} and status code is {response.status_code}")
