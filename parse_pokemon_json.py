import sys
import json
from pprint import pprint

with open('rocket_map_pokemon.json') as data_file:    
    data = json.load(data_file)

for i in range(1,357):
    s = str(i)
    #print data[s]['rarity']
    if data[s]['rarity'] == "Rare":
        print s + "," + data[s]['name']
    elif data[s]['rarity'] == "Very Rare":
        print s + "," + data[s]['name']
    elif data[s]['rarity'] == "Ultra Rare":
        print s + "," + data[s]['name']
        