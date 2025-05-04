# app/core/jwt_token.py
import requests
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "../config/data.json")
JWT_URL = "https://jwt-server-ruby.vercel.app/token?uid={uid}&password={password}"


def get_jwt(region: str):
    try:
        with open(DATA_FILE, "r") as f:
            creds = json.load(f)

        region = region.lower()
        if region not in creds:
            print(f"[ERROR] Region '{region}' not found in data.json")
            return None

        uid = creds[region]["uid"]
        password = creds[region]["password"]

        url = JWT_URL.format(uid=uid, password=password)

        response = requests.get(url)
        if response.status_code == 200:
            jwt_data = response.json()
            return jwt_data.get("token")
        else:
            print(f"[ERROR] JWT API failed with status {response.status_code}")
            return None
    except Exception as e:
        print(f"[JWT ERROR] {str(e)}")
        return None
