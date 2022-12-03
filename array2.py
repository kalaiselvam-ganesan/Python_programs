#   Array

# append() method is used to add the element in the array
# it will add the element in the last 
list1=["car","bike","cycle","Flight","Helipad"]
list1.append("bus")
print(list1)

# pop() method is used to remove the element in the array
list1=["car","bike","cycle","Flight","Helipad"]
list1.pop(3)
print(list1)

# pop() method is used to remove the element in the array
# suppose we doesn't mention the index in the pop, it remove the last element of array 
list1=["car","bike","cycle","Flight","Helipad"]
list1.pop()
print(list1)

#remove() method is alse used to remove the element in the array
# list allow the duplicate element
# in remove method it remove the first occurance of item  in the list
list1=["car","bike","car","cycle","Flight","Helipad"]
list1.remove("car")
print(list1)



#   output
"""
['car', 'bike', 'cycle', 'Flight', 'Helipad', 'bus']

['car', 'bike', 'cycle', 'Helipad']

['car', 'bike', 'cycle', 'Flight']

['bike', 'car', 'cycle', 'Flight', 'Helipad']
"""