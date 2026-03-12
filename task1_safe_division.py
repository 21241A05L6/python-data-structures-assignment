# Task 1: Safe Division

try:
    num = float(input("Enter numerator: "))
    den = float(input("Enter denominator: "))

    result = num / den

except ValueError:
    print("Invalid input. Please enter numbers only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Operation Complete")