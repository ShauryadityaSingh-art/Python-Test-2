def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print("Please Select the Operation: \n 1. Addition\n 2. Substraction\n 3. Multiplication\n 4. Division")

    choice=input("Please enter your choice (1/2/3/4). ")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {substract(num1, num2)}")
        elif choice == "3":
            print(f"{num1} X {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid option! Choose the correct option (1/2/3/4)")

    except ZeroDivisionError:
        print("Error : Cannot divide by zero.")

    except ValueError:
        print("Error : Invalid input. Please  enter numbers only.")




            

    

