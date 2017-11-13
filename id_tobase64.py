from base64 import b64encode

with open('gym_ids_base16.txt','r') as fd:
    lines = fd.readlines()
    
for l in lines:
    ln = l.strip()
    print b64encode(ln)
   