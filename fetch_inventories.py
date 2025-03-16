import requests
import json
import pandas as pd
import time

def fetch_categories(roblox_id: str):
    response = requests.get(f"https://inventory.roblox.com/v1/users/{roblox_id}/categories")
    categories = json.loads(response.content)['categories']
    return pd.DataFrame([{'Name': i.get('items')[0].get('displayName'), 'ID': i.get('items')[0].get('id')} for i in categories])

def fetch_inventory(roblox_id: str, category_id: str):
    response = requests.get(f"https://inventory.roblox.com/v1/users/{roblox_id}/inventory/{category_id}")
    response = json.loads(response.text)['data']
    responses = []
    for i in response:
        responses.append(json.loads(requests.get(f"https://catalog.roblox.com/v1/catalog/items/{i}/details?itemType=Asset").text))
        time.sleep(2)
    # responses = pd.DataFrame(responses, columns=["Items"])
    return responses

print(fetch_inventory("171322313", "2"))
