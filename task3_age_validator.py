# Task 3: Age Validator

def check_age(age):

    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")

    return "Valid age"


try:
    age = int(input("Enter age: "))
    print(check_age(age))

except ValueError as e:
    print("Error:", e)