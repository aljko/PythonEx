"""
Create a script that only displays a particular part of a string it receives. 
In other words, make it so that you are able to decide the exact character range (e.g. 2nd to 5th character) to be displayed.
""""
import sys
print(sys.argv[1][int(sys.argv[2])-1:int(sys.argv[3])])
