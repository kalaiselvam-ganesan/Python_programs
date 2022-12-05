# Ex_3

print("original string:")
# Fetting input from the user
a=input()
print("Enter the the number to Eliminate:")
# getting input from the user
n=int(input())
# getting length of the string
length=len(a)
if n<length:
    print(a[n:])



#   output
"""
original string:
pynative
Enter the the number to Eliminate:
2
native
"""