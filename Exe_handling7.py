# Exception handling

#The try block contains code that might throw an exception. 
# If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. 
# If no error occurs, the code in the except block doesn't run.

coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]
choice = int(input())

try:
	print(coffee[choice])
except:
	print("Invalid number")
finally:
	print("Have a good day")



#   output


"""
Espresso
Have a good day


Invalid number
Have a good day
"""