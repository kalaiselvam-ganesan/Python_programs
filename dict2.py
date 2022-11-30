# Dictionaries

# len() method used to define the length of the dictionaries
thisdict={
    "name":"kalai",
    "age":"22",
    "DOB":"july 8th"
}
print(len(thisdict))


# type() method is used to find the data type 
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
print(type(thisdict))

# it allow the all data type in dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th",
    "details":True,
    "friends":["boys","girls"]
}
print(thisdict)


# dict() constructor is used to create the dictoinaries
thisdict=dict(name="kalai",age=23,DOB="8th july")
print(thisdict)


#   output

#   3
#   <class 'dict'>
#   {'name': 'kalai', 'age': 22, 'DOB': 'july 8th', 'details': True, 'friends': ['boys', 'girls']}
#   {'name': 'kalai', 'age': 23, 'DOB': '8th july'}
