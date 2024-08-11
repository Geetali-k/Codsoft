choice = input("Enter your choice (Add/Sub/Mul/Div): ")

if choice in ('Add', 'Sub', 'Mul', 'Div'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 'Add':
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == 'Sub':
        print(num1, "-", num2, "=", num1 - num2)

    elif choice == 'Mul':
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == 'Div':
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")
else:
    print("Invalid Input")