#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        

PLACEHOLDER = "[name]"

with (open("Input/Names/invited_names.txt", mode="r") as name_data, 
     open("Input/Letters/starting_letter.txt", mode="r") as letter_data):
    names = name_data.readlines()
    letter = letter_data.read()
    
names = [name.strip for name in names]  # Strip can be used to eliminate blank spaces and unnused new lines

for name in names:
    new_letter = letter.replace(PLACEHOLDER,name) 
    letter_title = f"{name}´s letter.txt"
   
    with open(f"Output/ReadyToSend/{letter_title}", mode="w") as completed_letter:
        completed_letter.write(new_letter)