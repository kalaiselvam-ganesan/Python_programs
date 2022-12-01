# Function

# Function definition
# using (**) as means we dont know how many arguments passed into the function, 
# for that we include the ** infront of parameter name.
def my_function(**name):
    print("His last name is " + name["lname"])
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
my_function(fname = "Tobias", lname = "Refsnes")


#   output

#   His last name is Refsnes