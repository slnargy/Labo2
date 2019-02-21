import re

pattern = r'\+[0-9]{2}\s[0-9]{3}\s[0-9]{2}\s[0-9]{2}'

p = re.compile(pattern)

num = input('Entrez un numéro de téléphone : ')

print(p.match(num))
