import click
import json
import pprint

with open("achievements_simple.json", "r") as f:
    achievements = json.load(f)

@click.command()
@click.option('--keyword', prompt='Please enter a keyword',
    help='Enter a keyword to return a list of related Civ VI achievements.')
def keyword_search(keyword):
    for item in achievements:
        # allow partial matching
        for k in item["keywords"]:
            if keyword.lower() in k:
                click.echo("%s" % item["name"])
                click.echo("%s\n" % item["description"])

if __name__ == '__main__':
    keyword_search()