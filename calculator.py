# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error! Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operation! Please use +, -, *, or /."

# Taking user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

    # Perform the calculation and display the result
    result = calculate(num1, num2, operation)
    print(f"\nResult: {num1} {operation} {num2} = {result}")

except ValueError:
    print("Invalid input! Please enter numeric values.")
