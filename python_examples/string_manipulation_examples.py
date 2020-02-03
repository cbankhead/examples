# This is how we make a comment in python.

"""We can also do multiline
   comments like this.
"""

# And this is how we import libraries in Python
import json
import requests


# This is 'camelCase'.
# This is 'PascalCase.
# This is 'snake_case.
# For naming variables snake_case is considered more Pythonic.


###########################
### String Manipulation ###
###########################

# Why is sting manipulation important? Because manipulating data also know as 'munging' is usefull for formating, parsing, filtering, removing & inserting type operations.


# This is how we declare a String Literal variable in python.
my_string = " ,Whats up everyone!, "


# How do we check if our 'my_string' variable contains the type of data we think it contains?
print("What data type is contained in the 'my_string' variable?") # In python3 we use the 'print()' function to print output. Here we are sending output asking a question about what data type the 'my_string' variable contains.
print(type(my_string)) # Here we are checking the data type with the 'type()' function and then printing the data type contained in the 'my_string' variable.


print("Below we will print the variable 'my_string':")
print(my_string) # Here we are printing the 'my_string' variable.
print("\n") # Here we are printing a New Line, maybe we should have also added in a New Line above on line number 25.


print("Here is a multi-line string:")
print("""
Line one 
line two
line three
""")


print("What is the length of the 'my_string' variable with white space?")
print(len(my_string))
print("\r")  # Here we are printing a Carriage Return


print("What is the length of the 'my_string' variable with the white spaces removed from the start and end of the string?")
print(len(my_string.strip()))
my_string = my_string.strip()# Here we are striping the begining and end of the string of white space by using the built in strip() String Method.
print("\n") # And again here we are printing a New Line. We will be printing more than a few of these in this example.


print("Here is the 'my_string' variable in UPPER case:")
print(my_string.upper())
my_string = my_string.upper() # Here we are setting the string to upper case by using the built in upper() String Method
print("\n")


print("Here is the 'my_string' variable in lower case:")
print(my_string.lower())
my_string = my_string.lower() # Her we are setting the string to lower case by utilizing the built in lower() string Method
print("\n")


print("Here is the 'my_string' variable with the trailing comma removed:")
print(my_string.rstrip(", "))
my_string = my_string.rstrip(", ") # Here we are specifying that the space and comma be striped from the trailing/right side of the string.
print("\n")


print("Here is the 'my_string' variable with the starting comma removed:")
print(my_string.lstrip(","))
my_string = my_string.lstrip(",") # Here we are specifying that the comma be striped from the starting/left side of the string.
print("\n")


print("What is the first letter in the 'my_string' variable '(it is an array)'?")
print("The first character in my string is: " + my_string[0]) # Here we are printing text that we concatinated with the 'my_string' variable and printing the first character of the string (Arrays start at position 0 rather than 1).
print("Above we concatanated a string and our 'my_string' variable")
print("\n")


print("How can we split 'my_string' into multiple strings?:")
print(my_string.split(" ")) # Here were are spitting the sting in the 'my_string' variable into sub-stings.
print("\n")


print("How can we check if our string contains a word we are intersted in?")
check = "up" in my_string # This will return True or False depending on wether the word 'up' is found in within the 'my_string' variable.
print(check) #This returns the boolean value 'True' as the 'my_sting' variable does contain the word 'up'. 
print("\n")


print("We can also check for a condition where something is not found in a string")
if "down" not in my_string: # Here we are using an 'if' statement to check if the word 'down' is not found in the 'my_string' variable.
    print("'down' was not found")
print("\n")


print("Was the 'my_string' variable meant to be a question or statement?")
print("Looks like it was meant to be a question: " + my_string.replace('!', '?')) # Here we printed a concatenation of text with our string variable and replaced the '!' character with a '?' character.
my_string = my_string.replace("!", "?") # Here we replaced the '!' character with the '?' character in the 'my_string' variable.
print("\n")


print("What if we are only interested in a specific starting or endpoint in our 'my_sting' variable?:")
print("Our string variable contains what word staring at position Zero and ending at position Four? " +my_string[0:4]) # Here we are getting the first word in the 'my_string' variable by slicing the first five values contined in the 'my_string' variable.
print("\n")

print("What if we were interested in the last word in the 'my_string' variable?")
print("We could slice the 'my_string' variable from the last 8 characters by indexing from the end of the variable (negative indexing).")
print("Here is the word found from applying the negative index '(-9:-1)' to the 'my_string' variable: " + my_string[-9:-1].upper()) # Here we are getting the last word in the string by applying a negative index. We are also changing the result to upper case.
print("We aslo used the string upper() Method to convert the work to UPPER case.")
print("\n")


my_reply = "Not much bro!" # Setting a string variable with our reply to a question.
print("We can also format an existing string with placeholders that we want to contain other strings.")


print("Our question is: {}".format(my_string)) # Insert the variable 'my_string' that just happens to be a question into the '{}' placeholder.
print("Our answer is: {}".format(my_reply)) # Insert the variable 'my_reply' that just happens to be a answer to the question into the '{}' placeholder.
print("\n")

like_how = "like this"  # Add a new string variable
number_seven = 7  # Add a new int variable
print("We could also do a sting %s." % (like_how.upper())) # print text, concatenate string variable with values inserted via placeholders.

print("Or a string and a the number '%d' %s." % (number_seven, like_how.upper())) # print text, concatenate string variable & int variable with the values inserted via placeholders.
print("\n")

print("We could also use f-strings to place our variables into our string.") # This feature came out in Python3.6.
print(f"How might you ask? {like_how}.") # Use f-strings to insert the 'like_how' string variable into our print statement.
print(f"Better yet: {like_how.capitalize()}!") # Use f-strings to insert the 'like_how' string variable into our print statement and use the capitalize() String Method to capitalize the first letter of the 'like_how' string variable.
print("\n")


