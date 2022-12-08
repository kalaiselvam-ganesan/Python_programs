# Regular expression

# importing the regular expression module
# regular expression is sequence of charater that forms a search pattern.
import re
txt=" The world is filled with beauty and Wonders. "
# Find all lower case characters alphabetically between "a" and "m":
x=re.findall("[a-m]",txt)
print(x)
# if no math found , it will return a empty list.
# checking the condition of if-else
if x:
    print("YES..Matched")
else:
    print("NO,Not matched")




#   output

"""
['h', 'e', 'l', 'd', 'i', 'f', 'i', 'l', 'l', 'e', 'd', 'i', 'h', 'b', 'e', 'a', 'a', 'd', 'd', 'e']

YES..Matched

"""