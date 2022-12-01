# Function

# Function definition
# when we passing the null arguments 
# it will use the default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

# Function call
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



#   output

#I am from Sweden
#I am from India
#I am from Norway
#I am from Brazil
