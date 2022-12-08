# Regular expression

# importing the regular expression module
# regular expression is sequence of charater that forms a search pattern.
import re
txt=" The World is filled with beauty and Wonders. "
# split() method is used to return the string which is splited with white space
# You can control the number of occurrences by specifying the maxsplit parameter
#Split the string only at the 3 occurrence
x=re.split("\s",txt,3)
print(x)
# checking the condition of if-else
if x:
    print("YES..Matched")
else:
    print("NO,Not matched")



#   output

"""
  ['', 'The', 'World', 'is filled with beauty and Wonders. ']
  YES..Matched
"""
