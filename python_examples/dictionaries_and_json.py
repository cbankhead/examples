
import json

###
# Dictionary &
# What does JSON look like? How do we output JSON?
print("Print my python dictionary:")
print(my_dict)
print("JSON DUMPs - Print my python dict as JSON:")
print(json.dumps(my_dict))

# What does a python dictionary look like? How do we parse JSON into a python dictionary?
print("Print my JSON:")
print(my_json)
print("JSON LOADs - Print json as a python dictionary:")
print(json.loads(my_json))

# How do we know if we our trying to dump data that is already formated as JSON?
print("Oops we double json-ed our json:")
print(json.dumps(my_json))

# How can we output our JSON with an indent?
print("Pretty Format my Json:")
print(json.dumps(json.loads(my_json), indent=2))

# How can we output our JSON with sorted keys?
print("Pretty Format my Json & Sort by key:")
print(json.dumps(json.loads(my_json), indent=2, sort_keys=True))