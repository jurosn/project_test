def simple_calculator():
    print("Welcome to Simple Calculator!")
    print("You enter 'q' anytime to quit.")

    while True:
        num1 = input("Please enter the first number:\n")
        if num1.lower() == 'q':
            break
        op = input("Please choose (+ - * /):\n")
        if op.lower() == 'q':
            break
        num2 = input("Please enter the second number:\n")
        if num2.lower() == 'q':
            break

        try:
            num1 = float(num1)
            num2 = float(num2)

            if op == '+':
                print(f"{num1} + {num2} = ", num1+num2)
            elif op == '-':
                print(f"{num1} - {num2} = ", num1-num2)
            elif op == '*':
                print(f"{num1} * {num2} = ", num1*num2)
            elif op == '/':
                if num2 == 0:
                    print("Error: Dvision by Zero!")
                else:
                    print(f"{num1} / {num2} = ", num1/num2)
            else:
                print("Invalid operator!")    

        except Exception as e:
            print("Error: ", e)

        again = input("Do you want to calculate again? (y or n)\n")

        if again.lower() != 'y':
            break    

if __name__ == "__main__":
    simple_calculator()