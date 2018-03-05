import sqlite3
import json
from cmd import Cmd 

conn = sqlite3.connect(':memory:')

conn.execute("""
    create table achievements (
        name text,
        description text,
        keywords text
    );
    """)

with open("achievements_keywords.json", "r") as f:
    achievements_raw = json.load(f)

achievements = []

for achievement in achievements_raw:
    dict(name=achievement["displayName"], 
         description=achievement["description"],
         keywords=achievement["keywords"])

for a in achievements:
    print(a)