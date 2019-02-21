import re

pattern = r'^[1-9]?[A-Z]{3}[1-9]{3}|[1-9]{3}[A-Z]{3}$'

p = re.compile(pattern)

#XLLLDDD ou XDDDLLL,où L est une lettre et D est un chiffre, et X est un chiffre optionnel (entre 1 et 9).

plaque = input("Entrez une plaque d'immatriculation :")

print(p.match(plaque))
