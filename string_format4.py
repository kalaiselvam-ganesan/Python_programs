# String formatting

# Declaration of integers
#We can use a multiple declaration
a=45
d=1234
e=23
# Declaration of string
# You can add parameters inside the curly brackets to specify how to convert the value:
# we can access by using the index numbers
b="The number are {2},{0},{1}"
# format() is used to string format with the help of {} curly bracket
c=b.format(a,d,e)
print(c)


# Declaration of integers
#We can use a multiple declaration
a=45
d=1234
e=23
# Declaration of string
# You can add parameters inside the curly brackets to specify how to convert the value:
# we can access by using the index numbers
b="The number are {2},{0},{1:.2f}"
# format() is used to string format with the help of {} curly bracket
c=b.format(a,d,e)
print(c)

#   output

#   The number are 23,45,1234
#   The number are 23,45,1234.00
