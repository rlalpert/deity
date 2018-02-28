# import requests
# import os
import json

# dev_key = os.environ["STEAM_API_KEY"]
# civ_vi_id = "289070"
# url = "http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={key}&appid={appid}".format(key=dev_key, appid=civ_vi_id)

# civ_vi_info = requests.get(url)
# data = civ_vi_info.json()

# with open("achievements_full.json", "w") as f:
#     json.dump(data["game"]["availableGameStats"]["achievements"], f, sort_keys=True, indent=4)

with open("achievements_raw.json", "r") as f:
    data = json.load(f)

percentages = data["achievementpercentages"]["achievements"]

with open('achievements_percentages.json', 'w') as f:
    json.dump(percentages, f, sort_keys=True, indent=4)