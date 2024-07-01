import math

"""Afficher une valeur pour vérifier que le module est bien importé"""
x = math.pi
print(x)

"""Afficher toutes les méthodes et propriétés du module math"""
print(dir(math))

"""Distinguer les méthodes des propriétés"""
for i in dir(math):
    attr = getattr(math, i)
    if callable(attr):
        print("name:", i, "type: method")
    else:
        print("name:", i, "type: property")