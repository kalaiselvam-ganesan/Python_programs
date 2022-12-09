#datetime module 

# importing the datetime module
import datetime

# The date contains year, month, day, hour, minute, second, and microsecond.
x=datetime.datetime.now()

# returns the year without century
print(x.strftime("%y"))
# returns the year with century full-version
print(x.strftime("%Y"))
# returns the month 
print(x.strftime("%m"))
# it returns the AM-PM
print(x.strftime("%p"))


#   output

"""
22
2022
12
AM
"""