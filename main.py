print("Hello World!")
text_inputted = str(input("Start typing: "))
print("\n")
file_name = str(input("Enter file name and press ENTER: ")) + '.txt'
text_file = open(file_name, 'x')  # Will create a new file with the name
        
text_file = open(file_name, 'a')
text_file = text_file.write(
text_inputted)  #Write() command is used to write to file
  
print("\n")
print("File created.")