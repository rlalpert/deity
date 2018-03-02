import json

# dev_key = os.environ["STEAM_API_KEY"]
# civ_vi_id = "289070"


with open("achievements_keywords.json", "r") as f:
    items = json.load(f)

all_keywords = set()

for item in items:
    if "ch\u00e2teaux" in item["description"].lower():
        item.setdefault("keywords", []).append("ui-ch\u00e2teaux")
    # add all keywords to file
    if "keywords" in item.keys():
        for key in item["keywords"]:
            all_keywords.add(key)

with open("achievements_keywords.json", "w") as f:
    json.dump(items, f, sort_keys=True, indent=4)

all_keywords = list(all_keywords)
all_keywords.sort()

with open("keywords.txt", "w") as f:
    for keyword in all_keywords:
        f.write(str(keyword)+ "\n")