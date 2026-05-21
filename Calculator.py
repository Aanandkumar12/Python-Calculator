# =====================================
#       SIMPLE PYTHON CALCULATOR
# =====================================

# List to store calculation history
history = []

# Addition Function
def add(a, b):
    return a + b

# Subtraction Function
def subtract(a, b):
    return a - b

# Multiplication Function
def multiply(a, b):
    return a * b

# Division Function
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Power Function
def power(a, b):
    return a ** b

# Modulus Function
def modulus(a, b):
    return a % b

# Main Program
print("=" * 40)
print("WELCOME TO MY CALCULATOR")
print("=" * 40)

while True:

    # Menu
    print("\nChoose an Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. View History")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    # Exit Program
    if choice == "8":
        print("\nThanks for using my calculator!")
        break

    # View History
    elif choice == "7":

        print("\n==== HISTORY =====")

        if len(history) == 0:
            print("No calculations found yet.")

        else:
            for item in history:
                print(item)

    # Mathematical Operations
    elif choice in ["1", "2", "3", "4", "5", "6"]:

        try:
            # User Input
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))

            # Addition
            if choice == "1":
                result = add(first_number, second_number)
                operation = (
                    f"{first_number} + {second_number} = {result}"
                )

            # Subtraction
            elif choice == "2":
                result = subtract(first_number, second_number)
                operation = (
                    f"{first_number} - {second_number} = {result}"
                )

            # Multiplication
            elif choice == "3":
                result = multiply(first_number, second_number)
                operation = (
                    f"{first_number} × {second_number} = {result}"
                )

            # Division
            elif choice == "4":
                result = divide(first_number, second_number)
                operation = (
                    f"{first_number} ÷ {second_number} = {result}"
                )

            # Power
            elif choice == "5":
                result = power(first_number, second_number)
                operation = (
                    f"{first_number} ^ {second_number} = {result}"
                )

            # Modulus
            elif choice == "6":
                result = modulus(first_number, second_number)
                operation = (
                    f"{first_number} % {second_number} = {result}"
                )

            # Show Result
            print("\n==============")
            print(f"Result: {round(result, 2)}")
            print("================")

            print("\nCalculation completed successfully! ")

            # Save to history
            history.append(operation)

        except ValueError:
            print("\nOops! Invalid input entered. ")
            print("Please enter valid numbers only.")

    # Invalid Choice
    else:
        print("\nInvalid choice! Please try again.")
