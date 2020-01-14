"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

word_definitions["Pugilist"] = "Fighting with the fists; boxers, usually professionals."
word_definitions["Littoral"] = "Of or relating to the shore of a lake, sea, or ocean."
word_definitions["Gallimaufry"] = "A hodgepodge; jumble."
word_definitions["Lepidopterology"] = "Branch of zoology dealing with butterflies and moths."


"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print("Pugilist:", word_definitions["Pugilist"])
print("Littoral:", word_definitions["Littoral"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

# Bracket notation is used to access the value of the key.
for key in word_definitions:
    print(f"The definition of {key} is: {word_definitions[key]}\n")

# Tuple Unpacking- another way to do the same thing. 
# In Python Dictionary, items() method is used to return the list with all dictionary keys with values.
# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
for key, value in word_definitions.items():
    print(f"The definition of {key} is: {value}\n")