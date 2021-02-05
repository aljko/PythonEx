""""
Create a script that uses the len method to display the length of the string named: "string" below.
We want to count only characters, so ignore the number of spaces (without changing the string).
string = "Taumata whakatangihanga koauau o tamatea turi pukaka piki maungah oronuku pokai whenuaki tanatahu "
"""

import sys
print(len(sys.argv[1].replace(" ", "")))