import math

def text_based_calculator():
    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Trigonometry (sin, cos, tan)")
        print("6. Square Root (sqrt)")
        print("7. Square (sq)")
        print("8. Exponential (exp)")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == '9':
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", num1 + num2)
            elif choice == '2':
                print("Result:", num1 - num2)
            elif choice == '3':
                print("Result:", num1 * num2)
            elif choice == '4':
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error: Division by zero")

        elif choice in ['5']:
            trig_operation = input("Enter trigonometric function (sin, cos, tan): ")
            angle = float(input("Enter angle in radians: "))
            if trig_operation == 'sin':
                print("Result:", math.sin(angle))
            elif trig_operation == 'cos':
                print("Result:", math.cos(angle))
            elif trig_operation == 'tan':
                print("Result:", math.tan(angle))
            else:
                print("Invalid trigonometric function")

        elif choice == '6':
            num = float(input("Enter number: "))
            print("Result:", math.sqrt(num))

        elif choice == '7':
            num = float(input("Enter number: "))
            print("Result:", num * num)

        elif choice == '8':
            num = float(input("Enter number: "))
            print("Result:", math.exp(num))

        else:
            print("Invalid choice")

if __name__ == "__main__":
    text_based_calculator()