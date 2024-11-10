# Declaration of dictionarys

programming_dictionary = {           # This way you can put key and items in it at the start.
    "Bug": "An error of your mother",
    "Function": "Something that you arent",
    "Loop": "Your life",
    1: "A number can be used as key."
}

empty_dictionary = {}                # You can create a empty dictionary.



# Ways to print a dictionary.
print(programming_dictionary["Bug"]) # By key.
print(programming_dictionary[1])     # You can use number as a key, but not as an index

# Operation in dictionarys.

programming_dictionary[1] = "Wow, thats right." # You can replace values.  
programming_dictionary = {}          # This way you empty a dictionary.

# Loop through a dictionary:

for key in programming_dictionary:   # Only get keys of the dictionary.
    print(key)                        

for value in programming_dictionary.values: # Only get values of the dictionary.
    print(value)
    
for key,value in programming_dictionary.items: # Get key and the value.
    print(f"{key}: {value}")