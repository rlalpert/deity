import json

# dev_key = os.environ["STEAM_API_KEY"]
# civ_vi_id = "289070"


with open("achievements_keywords.json", "r") as f:
    items = json.load(f)

all_keywords = set()

for item in items:
    # if "australia".lower() in item["description"].lower():
    #     item.setdefault("keywords", []).append("civ-australia")
    # add all keywords to file
    if "keywords" in item.keys():
        for key in item["keywords"]:
            if key.startswith("gp-"):
                item["keywords"].remove(key)
                key = "great_person-" + key.split("-")[1]
                item["keywords"].append(key)
            all_keywords.add(key)

with open("achievements_keywords.json", "w") as f:
    json.dump(items, f, sort_keys=True, indent=4)

all_keywords = list(all_keywords)
all_keywords.sort()

with open("keywords.txt", "w") as f:
    for keyword in all_keywords:
        f.write(str(keyword)+ "\n")