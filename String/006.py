"""
Create a script that replaces one character with another and redisplays the modified string.
"""
import sys

susseyement = ""

for i in range(len(sys.argv[1])):
    if sys.argv[1][i] == "s":
        susseyement = susseyement + "s"
    else:
        susseyement = susseyement + sys.argv[1][i]


print(susseyement)