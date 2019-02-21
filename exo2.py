import sys
import re

filename = sys.argv[1] #argv=list

p=re.compile(r'\d+')

with open(filename) as f:
    content = f.readlines()
   

num = 0
for line in content:
    num += 1
    L = p.findall(line)
    if len(L) > 0 :
    
        print("line {}:".format(num), ", ".join(L))
