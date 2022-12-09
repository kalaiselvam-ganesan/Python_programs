#datetime module 

# importing the datetime module
import datetime

# The date contains year, month, day, hour, minute, second, and microsecond.
x=datetime.datetime.now()

# Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%w"))
# Day of month 01-31
print(x.strftime("%d"))
# month name - full-version
print(x.strftime("%B"))
# month name - short- version
print(x.strftime("%b"))


#   output

"""
5
09
December
Dec
"""