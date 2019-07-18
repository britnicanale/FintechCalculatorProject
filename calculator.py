#Calculator

def calculate():
    plus = False
    minus = False
    multiply = False
    divide = False
    exp = input("Write your expression below. Use numbers only\n ")
    numbers = []
    result= 0
    for i in exp:
        if i.isdigit():
            numbers.append(int(i))
        if i.isalpha():
            return "Sorry, characters must be numerical digits"
        if i == "+":
            plus = True
        if i == "-":
            minus = True
        if i == "*":
            multiply = True
        if i == "/":
            divide = True
    if plus:
        result = numbers[0] + numbers[1]
    elif minus:
        result = numbers[0] - numbers[1]
    elif multiply:
        result = numbers[0] * numbers[1]
    elif divide:
        result = numbers[0] / numbers[1]
    return result


print(calculate())