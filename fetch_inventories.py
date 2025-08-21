import requests
import json
import pandas as pd
import time

def fetch_categories(roblox_id: str):
    response = requests.get(f"https://inventory.roblox.com/v1/users/{roblox_id}/categories")
    categories = json.loads(response.content)['categories']
    return pd.DataFrame([{'Name': i.get('items')[0].get('displayName'), 'ID': i.get('items')[0].get('id')} for i in categories])

def fetch_inventory(roblox_id: str, category_id: str):
    response = requests.get(f"https://inventory.roblox.com/v2/users/{roblox_id}/inventory/{category_id}")
    items = []
    for i in json.loads(response.text)['data']:
        items.append((i['assetId'], i['assetName']))
    return pd.DataFrame(items)
