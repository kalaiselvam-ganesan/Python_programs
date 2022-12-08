# Regular expression

# importing the regular expression module
# regular expression is sequence of charater that forms a search pattern.
import re
txt="_ The world is filled with beauty and Wonders. "
# Searching the First occurance of white space.
x=re.search("\s",txt)
# printing the positon of white-space.
print("position:",x.start())
# checking the condition of if-else.
if x:
    print("YES..Matched")
else:
    print("NO,Not matched")



#   output

"""
position: 1
YES..Matched
"""