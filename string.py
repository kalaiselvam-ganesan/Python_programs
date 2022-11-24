#string function

a=" Hello world"
# convert a lower case into upper case
print(a.upper())
# convert a uppercase into lower case
print(a.lower())
# Remove the whitespace from the begining or end of the string
print(a.strip())
# Replace a charater or string in the particular place
print(a.replace("H","J"))
# split the string 
print(a.split(","))

#   output
#   HELLO WORLD
#    hello world
#   Hello world
#    Jello world
#   [' Hello world']
