# Lambda() function

# Function definition
def my_function(n):
    return lambda x:x*n

# passing a arguments to lambda function to preform a multiply operation
a=my_function(2)
print("Double the number:",a(15))
# passing a arguments to lambda function to preform a multiply operation
a=my_function(3)
print("Trible the number:",a(15))
# passing a arguments to lambda function to preform a multiply operation
a=my_function(4)
print("Quarduple the number:",a(15))
# passing a arguments to lambda function to preform a multiply operation
a=my_function(5)
print("Quntiple the number:",a(15))


#   output

#   Double the number: 30
#   Trible the number: 45
#   Quarduple the number: 60
#   Quntiple the number: 75
