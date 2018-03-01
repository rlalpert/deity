import json

# dev_key = os.environ["STEAM_API_KEY"]
# civ_vi_id = "289070"


with open("achievements_keywords.json", "r") as f:
    items = json.load(f)

for item in items:
    if "science" not in item["description"].lower() and "victory" in item["description"].lower() and "victory-science" in item["keywords"]:
        # item.setdefault("keywords", []).append("victory-religious")
        item["keywords"].remove("victory-science")

with open("achievements_keywords.json", "w") as f:
    json.dump(items, f, sort_keys=True, indent=4)