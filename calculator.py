#Calculator

def calculate(exp):
    plus = False
    minus = False
    multiply = False
    divide = False
    numbers = []
    b = 0
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
    return str(result)
    

def multi_calculate():
    exp = input("Write your expression below. Use numbers only\n ")
    digits = exp.split()
    while len(digits)>1:
        num = calculate(digits[0:3])
        digits.pop(0)
        digits.pop(0)
        digits.pop(0)
        digits.insert(0, num)
    return digits[0]

print(multi_calculate())