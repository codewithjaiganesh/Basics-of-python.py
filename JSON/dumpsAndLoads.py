import json
d = {
    "username": "johndoe123",
    "email": "john@example.com",
    "age": 28,
    "is_active": True
}


with open("data.json", "w") as f:
    js_data = json.dump(d,f,indent=8,sort_keys=True)


