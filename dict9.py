# Dictionaries

# nested dictionaries is created and printed
user={
    "user1":{
        "name":"kalai",
        "password":"kalai123"
    },
    "user2":{
        "name":"selvam",
        "password":"selavm123"
    },
    "user3":{
        "name":"ram",
        "password":"ram123"
    }
}
print(user)
print("\n")

# another way to create a nested dictionaries and printed
user1={
    "name":"kalai",
    "year":2018
}
user2={
    "name":"kamal",
    "year":2019
}
user3={
    "name":"sam",
    "year":2020
}
user={
    "user1":user1,
    "user2":user2,
    "user3":user3
}
print(user)


#   output

#{'user1': {'name': 'kalai', 'password': 'kalai123'}, 'user2': {'name': 'selvam', 'password': 'selavm123'}, 'user3': {'name': 'ram', 'password': 'ram123'}}


#{'user1': {'name': 'kalai', 'year': 2018}, 'user2': {'name': 'kamal', 'year': 2019}, 'user3': {'name': 'sam', 'year': 2020}}
 