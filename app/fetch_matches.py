import requests


def get_offer_matches(offer_id):
    url = f"http://localhost:5000/offer-matches/{offer_id}"
    headers = {"Auth": "827e8e1a-119c-48e2-af1c-cef81f933a5a"}

    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return None
    data = response.json()
    return data["matching_offers"]
