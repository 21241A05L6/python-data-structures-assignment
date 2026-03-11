# Task 6: Safe File Reading

import os

filename = input("Enter filename to open: ")

if os.path.exists(filename):

    with open(filename, "r") as file:
        print(file.read())

else:
    print("File not found. Please check the filename.")