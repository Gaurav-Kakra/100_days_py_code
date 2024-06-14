##Reading the names
with open("Input/Names/invited_names.txt",mode='r') as file:
    # Read all lines
    names = file.readlines()
    print(names)
    
with open("Input/Letters/starting_letter.txt",mode='r') as file:
    letter = file.read()
    for name in names:
        name = name.strip()
        new_letter = letter.replace("[name]",name)
        print(new_letter)
        with open(f"Output/letter_{name}.txt",mode='w') as outp:
            outp.write(new_letter)





    

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp