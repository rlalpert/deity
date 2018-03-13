import sqlite3
import json
from cmd import Cmd 
import pprint

with open("achievements_keywords.json", "r") as f:
    achievements_raw = json.load(f)

achievements = []

for achievement in achievements_raw:
    achievements.append(dict(name=achievement["displayName"], 
         description=achievement["description"],
         keywords=achievement["keywords"]))

# pprint.pprint(achievements)

for a in achievements:
    if "civ-rome" in a["keywords"]:
        pprint.pprint(a)