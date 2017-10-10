#!/usr/bin/python3

import requests
import json
import sys
import getopt

def usage():
    print("./get_pokemon_info.py -f <input-file> [-o <option>]")
    print("      -f <input-file>  :  single line for each pokemon name or id, make sure spelling is correct.")
    print("      -o <option>      :  0 = inputs is names, 1 = input is id numbers")
    
    
    
def main():
    filename = None
    poke_id = []
    poke_na = []
    option = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:ho:", ["help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-f":
            filename = a
        elif o == "-o":
            option = int(a)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"
    url = 'https://pokeapi.co/api/v2/pokemon/'
    with open(filename,'r') as myfile:
        for line in myfile:
            if '\'' in line:
                line = line.replace('\'',"")
            if '.' in line:
                line = line.replace('.','-')
            if ' ' in line:
                line = line.replace(" ","")
            line = line.rstrip('\r')
            line = line.rstrip('\n')
            if option is 0:
                line = line.lower()
                print(line)
                poke_na.append(str(line))
                get_url = url + line
                resp = requests.get(get_url)
                #print(resp)
                j = resp.json()
                poke_id.append(str(j['id']))
                print(j['id'])
            elif option is 1:
                poke_id.append(str(line))
                get_url = url + line
                resp = requests.get(get_url)
                j = resp.json()
                poke_na.append(str(j['name']))
                print(j['name'])
    print(poke_id)
    print(poke_na)
    combined = zip(poke_id,poke_na)
    list(combined)

if __name__ == "__main__":
    main()
