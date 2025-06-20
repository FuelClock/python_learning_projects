def calculator():
    number1 = float(input("Enter your first number:"))
    action = input("What action do you want to perform? +,-,*,/")
    number2 = float(input("Enter your second number:"))


    if action == "+":
        print(number1 + number2)
    elif action == "-":
        print(number1 - number2)
    elif action == "*":
        print(number1 * number2)
    elif action == "/":
        print(number1 /number2)
    close_calc = str(input("Do you wish to perform another calculation? Y/N"))

    if close_calc.upper() == "Y":
        calculator()
    elif close_calc.upper() != "Y":
        
        exit()

calculator()

    