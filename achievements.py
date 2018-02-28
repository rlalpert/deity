import requests
import os
import json

dev_key = os.environ["STEAM_API_KEY"]
civ_vi_id = "289070"
url = "http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={game_id}&format=json".format(game_id=civ_vi_id)

stats = requests.get(url)

with open('achievements_raw.json', 'w') as file:
    json.dump(stats.json(), file, sort_keys=True, indent=4)