#datetime module 

# importing the datetime module
import datetime

# The date contains year, month, day, hour, minute, second, and microsecond.
x=datetime.datetime.now()
print(x)
# it return the year
print(x.year)
# it return the weekday with full-version
print(x.strftime("%A"))
# it return the weekday with half-version
print(x.strftime("%a"))



#   output


"""
2022-12-09 10:35:28.964576
2022
Friday
Fri
"""