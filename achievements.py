import json

# dev_key = os.environ["STEAM_API_KEY"]
# civ_vi_id = "289070"


with open("achievements_keywords.json", "r") as f:
    items = json.load(f)

for item in items:
    if "great wall" in item["description"].lower():
        item.setdefault("keywords", []).append("ui-great_wall")

with open("achievements_keywords.json", "w") as f:
    json.dump(items, f, sort_keys=True, indent=4)