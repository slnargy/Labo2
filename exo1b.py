import re

pattern = r'-?[1-9][0-9]*'

p = re.compile(pattern)

nb = input('Entrez un nombre entier non nul :')

print(p.match(nb))
