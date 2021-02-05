"""
Create a script that takes a string as one parameter and a character as another parameter. Your script should return the position (starting with 1 and not 0) of all occurrences of the character within the string.
For example, for the word "hello" and for the character "o", the script will return :
- "position : 5"
"""

import sys

sortie = ""

for i in range(len(sys.argv[1])):
    if sys.argv[1][i] == sys.argv[2]:
        sortie = sortie + str(i + 1) + " "

print(sortie)