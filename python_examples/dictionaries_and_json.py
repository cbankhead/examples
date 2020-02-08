#######################
# Dictionary & JSON ###
#######################


my_dict = {"1": "one", "2": "two", "3": "three"}
my_json = '{"1": "one", "2": "two", "3": "three", "z": "zebra", "y": "yellow", "x": "x-ray", "bool1": True, "bool2": False, "int1": 1, "int2": 2}'

# A dictionary has keys and corresponding values.
my_dict["4"] = "four" # Here we are adding a fourth key/value pair to our 'my_dict" variable.
print(my_dict)

# What does JSON look like? How do we output JSON?
print("Print my python dictionary:")
print(my_dict)
print("\n")


print("JSON DUMPs - Print my python dict as JSON:")
print(json.dumps(my_dict))
print("\n")


# What does a python dictionary look like? How do we parse JSON into a python dictionary?
print("Print my JSON:")
print(my_json)
print("\n")
print("JSON LOADs - Print json as a python dictionary:")
print(json.loads(my_json))
print("\n")


# How do we know if we our trying to dump data that is already formated as JSON?
print("Oops we double json-ed our json:")
print(json.dumps(my_json))
print("\n")


# How can we output our JSON with an indent?
print("Pretty Format my Json:")
print(json.dumps(json.loads(my_json), indent=2))
print("\n")


# How can we output our JSON with sorted keys?
print("Pretty Format my Json & Sort by key:")
print(json.dumps(json.loads(my_json), indent=2, sort_keys=True))
print("\n")