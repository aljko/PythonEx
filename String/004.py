"""
Find 3 ways to return the following string without including the spaces at the beginning and the end: "Data Analyst".
"""
import sys

print(sys.argv[1].replace(" ", ""))

print(sys.argv[1].strip())

arg = sys.argv[1]
while arg[0] == " ":
    arg = arg[1:]
while arg[-1] == " ":
    arg = arg[:-1]
print(arg)