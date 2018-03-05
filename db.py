import sqlite3
import json
from cmd import Cmd 
import pprint

# conn = sqlite3.connect(':memory:')

# conn.execute("""
#     create table achievements (
#         name text,
#         description text,
#         keywords text
#     );
#     """)

with open("achievements_keywords.json", "r") as f:
    achievements_raw = json.load(f)

achievements = []

for achievement in achievements_raw:
    achievements.append(dict(name=achievement["displayName"], 
         description=achievement["description"],
         keywords=achievement["keywords"]))

pprint.pprint(achievements)