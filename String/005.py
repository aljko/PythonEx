"""
Create a script that converts all vowels to uppercase and all consonants to lowercase.
"""
import sys

sortie = ""

for i in range(len(sys.argv[1])):
    if sys.argv[1][i] in "aeiouyAEIOUY":
        sortie = sortie + sys.argv[1][i].upper()
    elif sys.argv[1][i] in "bcdfghjklmnpqrstvwxzABDEFGHIJKLMNOPQRSTUVWXYZ":
        sortie = sortie + sys.argv[1][i].lower()

print(sortie)