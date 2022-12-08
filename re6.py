# Regular expression

# importing the regular expression module
# regular expression is sequence of charater that forms a search pattern.
import re
txt=" The World is filled with beauty and Wonders. "
# split() method is used to return the string which is splited with white space
x=re.split("\s",txt)
print(x)
# checking the condition of if-else
if x:
    print("YES..Matched")
else:
    print("NO,Not matched")



#   output

"""
    ['', 'The', 'World', 'is', 'filled', 'with', 'beauty', 'and', 'Wonders.', '']
    YES..Matched
"""