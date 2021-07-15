'''
Create a script that does the same thing as the insert method, but at a random position.
'''
import sys
import random

liste = sys.argv[2:]
index = random.randint(0,len(liste))
liste.insert(index, sys.argv[1])

print(liste)