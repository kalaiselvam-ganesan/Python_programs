# del() method is used to delete the value in the list using index and slice
thislist=["apple","suji",'kalai',40.6,True]
del thislist[1]
print(thislist)

# del() method is used to delete the value in the list using index and slice
thislist=["apple","suji",'kalai',40.6,True]
del thislist[1:3]
print(thislist)

# del() method is used to delete the value in the list using index and slice
thislist=["apple","suji",'kalai',40.6,True]
del thislist
print(thislist)

# Clear() method is used to clear the entire list
thislist=["apple","suji",'kalai',40.6,True]
thislist.clear()
print(thislist)

#loop in the list
thislist=["apple","suji",'kalai',40.6,True]
for i in thislist:
    print(i)


#   output
#   ['apple', 'kalai', 40.6, True]
#   ['apple', 40.6, True]
#   []
#   apple
#   suji
#   kalai
#   40.6
#   True
