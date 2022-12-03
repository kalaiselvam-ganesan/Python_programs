#   array

# A list of value stored in a single variable, now it represent the array 
list1=["car","bike","cycle","Flight","Helipad"]
print(list1)

# we can access a array with the index number
# which the index starts with 0,1,2,3,4,5....etc
list1=["car","bike","cycle","Flight","Helipad"]
print(list1[0],list1[3])

# we can modify the array using index number
list1=["car","bike","cycle","Flight","Helipad"]
list1[0]="bus","coin"
print(list1)

# len() method is used to find the langth of array
list1=["car","bike","cycle","Flight","Helipad"]
print(len(list1))
print("\n")

# we can loop the array using the for loop
list1=["car","bike","cycle","Flight","Helipad"]
for x in list1:
    print(x)


#   output
"""
['car', 'bike', 'cycle', 'Flight', 'Helipad']

car Flight

[('bus', 'coin'), 'bike', 'cycle', 'Flight', 'Helipad']

5

car
bike
cycle
Flight
Helipad
 """ 