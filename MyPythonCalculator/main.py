import logo


def multiplication(n1, n2):
    return float(n1 * n2)


def division(n1, n2):
    return float(n1 / n2)


def addition(n1, n2):
    return float(n1 + n2)


def subtraction(n1, n2):
    return float(n1 - n2)


def Calculator():
    print(test.Logo)
    Cal_dic = {}
    keep_going = True

    while keep_going:
        if not Cal_dic:
            user_firstN = float(input("What is the first number?: "))
            num1 = user_firstN
        else:
            num1 = Cal_dic["result"]

        user_operator = input("""*
# /
# +
# -
# choose your operation: """)

        user_secondN = float(input("What is your second number?: "))

        if user_operator == "*":
            Cal_dic["result"] = multiplication(num1, user_secondN)
        elif user_operator == "/":
            Cal_dic["result"] = division(num1, user_secondN)
        elif user_operator == "+":
            Cal_dic["result"] = addition(num1, user_secondN)
        elif user_operator == "-":
            Cal_dic["result"] = subtraction(num1, user_secondN)

        user_next_calculation = input(
            f"Type 'yes' to calculate with {Cal_dic['result']} or 'no' for a new calculation: ").lower()

        if user_next_calculation == "no":
            keep_going = False


# Start the calculator
Calculator()
