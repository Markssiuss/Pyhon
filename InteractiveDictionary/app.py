import json
import os

if os.path.exists("data.json"):
    data = json.load(open("data.json"))
    print(data["rain"])

