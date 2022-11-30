# Dictionaries

# in for loop we printing the keys in dictionaries 
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
for i in thisdict:
    print(i)
print("\n")

# keys()  method in for loop to print the keys in dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
for i in thisdict.keys():
    print(i)
print("\n")

# in for loop we printing the value pair in the dictionaries 
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
for i in thisdict:
    print(thisdict[i])
print("\n")

# values() method in for loop to print the values in  dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
for i in thisdict.values():
    print(i)
print("\n")

# item() method in for loop to print the items in the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
for i in thisdict.items():
    print(i)
print("\n")


# output

"""name
age
DOB


name
age
DOB


kalai
22
july 8th


kalai
22
july 8th


('name', 'kalai')
('age', 22)
('DOB', 'july 8th')"""