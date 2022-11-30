# Dictionaries

# pop() method is used to remove the item in the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
thisdict.pop("age")
print(thisdict)

# popitem() method is used to remove the last inserted item in the dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
thisdict.popitem()
print(thisdict)

# del() method used to delete the particular item in the dictionaries if the key is mentioned.
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
del thisdict["name"]
print(thisdict)

# del() method is used to delete the entrie dictionaries
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
del thisdict
print(thisdict)

# clear() method is used to clear the dictionaries but {} it will remains
thisdict={
    "name":"kalai",
    "age":22,
    "DOB":"july 8th"
}
thisdict.clear()
print(thisdict)


#   output

#   {'name': 'kalai', 'DOB': 'july 8th'}
#   {'name': 'kalai', 'age': 22}
#   {'age': 22, 'DOB': 'july 8th'}
#   {}