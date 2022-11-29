# Set

# in pop() method used to remove item in the last
# but in set it is unordered so it can remove any item in set 
thisset={"kalai","selvam",23.0,45}
thisset.pop()
print(thisset)

# clear() method used to clear items in set 
thisset={"kalai","selvam",23.0,45}
thisset.clear()
print(thisset)

# del() method is used to delete the set completely 
thisset={"kalai","selvam",23.0,45}
del thisset
print(thisset)

# for loop in set
thisset={"kalai","selvam",23.0,45}
for i in thisset:
    print(i)


#   output

#   {45, 'kalai', 23.0}

#   set()

#   selvam
#   45
#   kalai
#   23.0
