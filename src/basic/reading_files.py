


## reading and writting
from os import close


file_example = open("example.txt", "r+")

# creates an array
print(file_example.readlines()[2])

file_example.close()
 

### -------

file_example = open("example.txt", "r+")

# reads the whole file
print(file_example.read())

# Appends whatever you do to the end of the file
file_example.write("o\n")

file_example.close()


