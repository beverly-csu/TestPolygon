import json

with open('notes.json', 'r') as file:
    print(json.load(file))