import sys
import json
from pprint import pprint

def create_pgan_command(poke_list, iv="", lvl=""):
    str__pgan = "!set " 
    str_pgan_iv = iv
    str_pgan_lvl = lvl   
    for i in poke_list:
        if str_pgan_iv != "" and str_pgan_lvl == "":
            str__pgan = str__pgan + i + " " + str_pgan_iv + ","
        elif str_pgan_iv == "" and str_pgan_lvl != "":
            str__pgan = str__pgan + i + " " + str_pgan_lvl + ","
        elif str_pgan_iv != "" and str_pgan_lvl != "":
            str__pgan = str__pgan + i + " " + str_pgan_iv + " " + str_pgan_lvl + ","
        else:
            str__pgan = str__pgan + i + ", "
    print str__pgan

rare_list = []
very_rare_list = []
ultra_rare_list = []

with open('rocket_map_pokemon.json') as data_file:    
    data = json.load(data_file)

for i in range(1,357):
    s = str(i)
    #print data[s]['rarity']
    if data[s]['rarity'] == "Rare":
        print s + "," + data[s]['name']
        rare_list.append(data[s]['name'])
    elif data[s]['rarity'] == "Very Rare":
        print s + "," + data[s]['name']
        very_rare_list.append(data[s]['name'])
    elif data[s]['rarity'] == "Ultra Rare":
        print s + "," + data[s]['name']
        ultra_rare_list.append(data[s]['name'])
    
print create_pgan_command(rare_list)
print create_pgan_command(very_rare_list)
print create_pgan_command(ultra_rare_list)