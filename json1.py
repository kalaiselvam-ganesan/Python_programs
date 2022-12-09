# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

#importing the json module
import json

# convert json to python
x='{"name":"kalai","age":23,"blood grp":"B+"}'
y=json.loads(x)
# it returns as dictionary
print(y["name"])



#   output

# kalai