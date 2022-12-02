# Recursion function

# function definition
def recursion(k):
    #condtion checking of if-else
  if(k>0):
    result=k+recursion(k - 1)
    print(result)
  else:
    result=0
  return result

print("\nRecursion Results\n")
# function call of recursion
recursion(6)



#      output

"""Recursion Example Results
1
3
6
10
15
21"""