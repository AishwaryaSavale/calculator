def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    while True:
        print("\nOptions:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        if choice == '1':
            print("Result is :", add(num1, num2))
        elif choice == '2':
            print("Result is :", subtract(num1, num2))
        elif choice == '3':
            print("Result is :", multiply(num1, num2))
        elif choice == '4':
            print("Result is :", divide(num1, num2))
        else:
            print("Invalid Input! Please enter a valid choice.")

        continue_choice = input("Do you want to continue? (yes/no): ")
        if continue_choice.lower() != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

calculator()


