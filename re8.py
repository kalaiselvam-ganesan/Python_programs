# Regular expression

# importing the regular expression module
# regular expression is sequence of charater that forms a search pattern.
import re
txt="_ The world is filled with beauty and Wonders. "
# Replace all white-space characters with the digit "9"
x=re.sub("\s","9",txt)
print(x)
# checking the condition of if-else
if x:
    print("YES..Matched")
else:
    print("NO,Not matched")
print("\n")



#   output

"""
 _9The9world9is9filled9with9beauty9and9Wonders.9
 YES..Matched
"""
