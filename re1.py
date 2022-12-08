# Regular expression

# importing the regular expression module
# regular expression is sequence of charater that forms a search pattern.
import re
txt=" The world is filled with beauty and Wonders. "
x=re.search("The.*Wonder",txt)
# checking the condition of if-else
if x:
    print("YES..Matched")
else:
    print("NO,Not matched")



#   output

"""
    YES..Matched
"""