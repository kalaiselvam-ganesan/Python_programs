# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

#importing the json module
import json

# converting python to json
x={
    "name":"kalai",
    "age":23,
    "Blood grp":"B+",
    "married":False,
    "divorced": False,
    "Friends":("ajay","sam"),
    "pets":None,
    "car":[
        {"model": "BMW 320","year":2018},
        {"model":"Audi A6","year":2019}
        ]
}
# we are using the parameter to indent the output
print(json.dumps(x,indent=4))


#   output

"""
{
    "name": "kalai",
    "age": 23,
    "Blood grp": "B+",
    "married": false,
    "divorced": false,
    "Friends": [
        "ajay",
        "sam"
    ],
    "pets": null,
    "car": [
        {
            "model": "BMW 320",
            "year": 2018
        },
        {
            "model": "Audi A6",
            "year": 2019
        }
    ]
}
"""
