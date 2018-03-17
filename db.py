import sqlite3
import json
from cmd import Cmd 
import pprint

with open("achievements_simple.json", "r") as f:
    achievements = json.load(f)

# pprint.pprint(achievements)

# for a in achievements:
#     if "civ-rome" in a["keywords"]:
#         pprint.pprint(a)