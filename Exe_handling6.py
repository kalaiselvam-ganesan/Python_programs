# Exception handling

#The try block contains code that might throw an exception. 
# If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. 
# If no error occurs, the code in the except block doesn't run.

try:
  print(1)
except:
  print(2)
finally:
  print(3)


#   output

# 1
# 3