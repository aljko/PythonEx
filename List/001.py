"""
Create a script that takes a list and displays only the elements (and their position) that have positions that are even (0, 2, 4, 6...).

Example list = ["a", "b", "c", "d", "e"], the function should return : 
- a position 0
- c position 2
- e position 4
"""
import sys

del sys.argv[0]
list =  sys.argv

for i in range(len(list)):
    if i%2 == 0:
        print(list[i])