# Lambda() function

# list of values 
a=[1,2,3,4,5,6,7,8,9,10]
print("Original list of integer:")
print(a)
# using lambda to identity the Even number
b=list(filter(lambda x:x%2==0,a))
print("Even number from said list:")
print(b)
# using lambda to identity the odd number
c=list(filter(lambda x:x%2!=0,a))
print("Odd number from siad list:")
print(c)


#   output

"""Original list of integer:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even number from said list:
[2, 4, 6, 8, 10]
Odd number from siad list:
[1, 3, 5, 7, 9]"""