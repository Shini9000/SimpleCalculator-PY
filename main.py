# Function for addition
def addition(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for divition
def divide(x, y):
    return x / y

print(f"Select a option to begin\n"
      f"1. Addition\n"
      f"2. Subtraction\n"
      f"3. Multiply\n"
      f"4. Divide\n")

while True:
    # Take user input
    choice = input(f"Select 1,2,3,4: ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input(f"Enter first number: "))
            num2 = float(input(f"Enter second number: "))
        except ValueError:
            print(f"Invalid input. Please enter a number.")
            continue
        match choice:
            case '1':
                print(num1, "+", num2, "=", addition(num1, num2))
            case '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            case '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            case '4':
                print(num1, "/", num2, "=", divide(num1, num2))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input(f"Let's do next calculation? (Y/N): ").capitalize()
        if next_calculation == "N":
            break
    else:
        print(f"Invalid Input")
