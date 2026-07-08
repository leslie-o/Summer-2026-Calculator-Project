print("Welcome to Calculator, as of rn, sometimes you may only use 2 numbers at a time sorry.")
print("We have access to: * , + , - , / , % , Power, Gradient ")



def number():
    process = input("What would you like to do? ")

    if process in ("*", "+", "-", "/", "%", "Power", "power", "Gradient", "gradient", "Grad", "grad"):
        num1 = float(input("Enter your desired (base/X1) value: "))
        num2 = float(input("Enter your desired (exponent/Y1) value: "))
        num3 = float(input("Enter your desired value (X2) (can be 0): "))
        num4 = float(input("Enter your desired value (Y2) (can be 0): "))
        answer_mul = num1 * num2
        answer_add = num1 + num2
        answer_sub = num1 - num2
        answer_div = num1 / num2
        answer_mod = num1 % num2
        answer_exp = (num1) ** (num2)
        answer_grad = (num4 - num2) / (num3 - num1)

    if process == "*":
        print("Multiplication it is then!", answer_mul)
    elif process == "+":
        print("Addition it is then!", answer_add)

    elif process == "-":
        print("Subtraction it is then!", answer_sub)
    elif process == "/":
        print("Division it is then!", answer_div)
    elif process == "%":
        print("Modulo it is then!", answer_mod)
    elif process in ("Power", "power"):
        print("Exponentiation it is then!", float(answer_exp))
    elif process in ("Gradient", "gradient", "Grad", "grad"):
        print("Here's the gradient!:", answer_grad)

        
def again():
    go_again = input("Would you like to keep going? Yes or No (say either of them) ")
    while go_again in ("Yes", "yes"):
        number()
        go_again = input("Would you like to keep going? Yes or No (say either of them) ")

    if go_again in ("No", "no"):
        print("The End")
    else:
        print("quit playing and do some maths")


number()
again()
