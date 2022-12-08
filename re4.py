# Regular expression

# importing the regular expression module
# regular expression is sequence of charater that forms a search pattern.
import re
txt=" The World is filled with beauty and Wonders. "
# Return a list containing every occurrence of "wo":
# if no math found , it will return a empty list.
x=re.findall("wo",txt)
print(x)
# checking the condition of if-else
if x:
    print("YES..Matched")
else:
    print("NO,Not matched")




#   output
"""
  []
  NO,Not matched
"""