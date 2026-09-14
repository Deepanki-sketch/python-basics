def Calculator():
    '''This is a calculator that can perform arithmetic operations on two numbers based on user input, it can perform addition, subtraction, division and multiplication.'''

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Error: Division by zero"

    if choice == '1':
     print(f"The result of addition is: {addition}")
    elif choice == '2':   
     print(f"The result of subtraction is: {subtraction}")
    elif choice == '3':
     print(f"The result of multiplication is: {multiplication}")
    elif choice == '4':
     print(f"The result of division is: {division}")

Calculator()     