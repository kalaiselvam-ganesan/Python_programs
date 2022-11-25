# copying the list of value to another list using copy() method
thislist=[100,20,10,50,70,30,60,40]
mylist=thislist.copy()
print(mylist)

# copying the list of value to another list using copy() method
# another method to copy the list
thislist=[100,20,10,50,70,30,60,40]
mylist=list(thislist)
print(mylist)

# Joining the two list into a single list
list1=["kalai","suji","kamal","alex"]
list2=[10,20,30,40]
list3=list1+list2
print(list3)

# joining the list using the append() method
list2=["kalai","suji","kamal","alex"]
list1=[10,20,30,40]
for x in list2:
    list1.append(x)
print(list1)

# Extend the list using extend() Method
list1=["kalai","suji","kamal","alex"]
list2=[10,20,30,40]
list1.extend(list2)
print(list1)


#   ouput
#   [100, 20, 10, 50, 70, 30, 60, 40]
#   [100, 20, 10, 50, 70, 30, 60, 40]
#   ['kalai', 'suji', 'kamal', 'alex', 10, 20, 30, 40]
#   [10, 20, 30, 40, 'kalai', 'suji', 'kamal', 'alex']
#   ['kalai', 'suji', 'kamal', 'alex', 10, 20, 30, 40]
