import sys
import json
from pprint import pprint

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
    
str_rare_pgan = "!set " 
str_pgan_iv = ""
str_pgan_lvl = ""   
for i in rare_list:
    if str_pgan_iv != "" and str_pgan_lvl == "":
        str_rare_pgan = str_rare_pgan + i + " " + str_pgan_iv + ","
    elif str_pgan_iv == "" and str_pgan_lvl != "":
        str_rare_pgan = str_rare_pgan + i + " " + str_pgan_lvl + ","
    elif str_pgan_iv != "" and str_pgan_lvl != "":
        str_rare_pgan = str_rare_pgan + i + " " + str_pgan_iv + " " + str_pgan_lvl + ","
    else:
        str_rare_pgan = str_rare_pgan + i + ", "
print str_rare_pgan

str_very_rare_pgan = "!set " 
str_pgan_iv = ""
str_pgan_lvl = ""   
for i in very_rare_list:
    if str_pgan_iv != "" and str_pgan_lvl == "":
        str_very_rare_pgan = str_very_rare_pgan + i + " " + str_pgan_iv + ","
    elif str_pgan_iv == "" and str_pgan_lvl != "":
        str_very_rare_pgan = str_very_rare_pgan + i + " " + str_pgan_lvl + ","
    elif str_pgan_iv != "" and str_pgan_lvl != "":
        str_very_rare_pgan = str_very_rare_pgan + i + " " + str_pgan_iv + " " + str_pgan_lvl + ","
    else:
        str_very_rare_pgan = str_very_rare_pgan + i + ", "
print str_very_rare_pgan

str_ultra_rare_pgan = "!set " 
str_pgan_iv = ""
str_pgan_lvl = ""   
for i in ultra_rare_list:
    if str_pgan_iv != "" and str_pgan_lvl == "":
        str_ultra_rare_pgan = str_ultra_rare_pgan + i + " " + str_pgan_iv + ","
    elif str_pgan_iv == "" and str_pgan_lvl != "":
        str_ultra_rare_pgan = str_ultra_rare_pgan + i + " " + str_pgan_lvl + ","
    elif str_pgan_iv != "" and str_pgan_lvl != "":
        str_ultra_rare_pgan = str_ultra_rare_pgan + i + " " + str_pgan_iv + " " + str_pgan_lvl + ","
    else:
        str_ultra_rare_pgan = str_ultra_rare_pgan + i + ", "
print str_ultra_rare_pgan