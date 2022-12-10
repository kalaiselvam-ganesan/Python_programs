# Exception handling

#The try block contains code that might throw an exception. 
# If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. 
# If no error occurs, the code in the except block doesn't run.

try:
    print("Heloo")
    var=10
    print(var/0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("Code run whatever happen")



#   output

"""
Heloo
Divided by zero
Code run whatever happen
"""