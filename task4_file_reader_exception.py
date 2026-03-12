# Task 4: File Reader

filename = input("Enter filename: ")

try:

    with open(filename, "r") as file:

        for i in range(3):
            print(file.readline().strip())

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")

finally:
    print("File operation attempted.")