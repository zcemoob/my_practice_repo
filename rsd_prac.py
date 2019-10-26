import json

my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relationships": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relationships": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relationships": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relationships": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}
print(type(my_group))

# converts file into JSON string
file_as_string = json.dumps(my_group, indent=4)

# write data in a file called my_file.json
with open('my_file.json', 'w') as dest:
    dest.write(file_as_string)

# opens and reads file (as a stream?)
with open('my_file.json', 'r') as source:
    file_contents = source.read()

print(file_contents)

# parses the JSON string back to a python object (e.g dict)
my_group_back_as_dict = json.loads(file_contents)

# e.g. getting output from file
print(my_group_back_as_dict['Nash']['job'])  # nash's job
print(my_group_back_as_dict['Jill']['relationships'])   # jill's relationships


