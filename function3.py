# Functions

# Function definition
# using (*) as means we dont know how many arguments passed into the function, for that we include the * infront of parameter name.
def my_function(*name):
    print("The youngest child is " + name[2])
# This way the function will receive a tuple of arguments, and can access the items accordingly:
my_function("Emil", "Tobias", "Linus")


#   output

#   The youngest child is Linus