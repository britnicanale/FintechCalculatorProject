#Calculator

def calculate():
    plus = False
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
    if plus:
        result = numbers[0] + numbers[1]
    # elif minus:
    #     result = a - b
    # elif multiply:
    #     result = a * b
    # elif divide:
    #     result = a / b
    return result


print(calculate())