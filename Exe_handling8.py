# Exception handling

#The try block contains code that might throw an exception. 
# If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. 
# If no error occurs, the code in the except block doesn't run.

try:
    num=5/0
except:
  print("An occured Error")
  # raise statement raise the exception what exception is occured
  raise


#   output

"""
An occured Error

Traceback (most recent call last):
File "<string>", line 8, in <module>
ZeroDivisionError: division by zero
"""