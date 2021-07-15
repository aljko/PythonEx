'''
Create a list, then add an element to the end of a list and remove 
the first element so that the list stays the same size.
'''
import sys

liste = sys.argv[3:]
liste.append(sys.argv[1])
print(liste)
