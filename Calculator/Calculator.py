while True:
    try:
        operator = input("Enter Operation (+, -, *, /, % or quit):")

        if operator.lower() == "quit":
            print("Thank you for using our simple calculator :)")
            break
        if operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "%":
            print("Invalid Operator!!")
            continue

        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter first number:"))

        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            print(num1 / num2)
        elif operator == "%":
            print(num1 % num2)
    except Exception as e:
        print("Please enter a valid operation")

