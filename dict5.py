# Dictionaries

# changing the value in the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
thisdict["age"]=24
print(thisdict)

# update() method alo used to update or change the value in dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
thisdict.update({"age":30})
print(thisdict)

# ading the element in the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
thisdict["colour"]="black"
print(thisdict)

# update() method is also used to add the element in the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
thisdict.update({"Friends":"boys"})
print(thisdict)


#   output

#   {'name': 'kalai', 'age': 24, 'DOB': 'july 8th'}
#   {'name': 'kalai', 'age': 30, 'DOB': 'july 8th'}
#   {'name': 'kalai', 'age': 22, 'DOB': 'july 8th', 'colour': 'black'}
#   {'name': 'kalai', 'age': 22, 'DOB': 'july 8th', 'Friends': 'boys'}
