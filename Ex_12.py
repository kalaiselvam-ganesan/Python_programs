# Ex_12

# declaration of nested dictionary
Dict1 = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# understand how to located the nested key
# Dict1['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# Dict1['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# Dict1['class']['student']['marks'] = {'physics': 70, 'history': 80}

print(Dict1['class']['student']['marks']['history'])


#   output

#   80