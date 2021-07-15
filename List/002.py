"""
We have a list. Create a script to replace the value of an element with another simply by indicating its position.
For example, we want to change the value of the third element of the list below:
"""
import sys

positionAModifier = int(sys.argv[1])
nouvelleValeur = sys.argv[2]
list = sys.argv[3:]

print("Ancienne liste")
print(list)

print("Nouvelle liste")
list[positionAModifier] = nouvelleValeur
print(list)