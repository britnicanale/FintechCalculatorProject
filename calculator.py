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
        try:
            i = float(i)
        except ValueError:
            pass
        if isinstance(i, float):
            numbers.append(int(i))
        elif i.isalpha():
            return "Sorry, characters must be numerical digits"
        elif i == "+":
            plus = True
        elif i == "-":
            minus = True
        elif i == "*":
            multiply = True
        elif i == "/":
            divide = True
    print(numbers)
    if plus:
        result = numbers[0] + numbers[1]
    elif minus:
        result = numbers[0] - numbers[1]
    elif multiply:
        result = numbers[0] * numbers[1]
    elif divide:
        result = numbers[0] / numbers[1]
    else:
        return "Sorry, this statement is invalid"
    return str(result)
    

def multi_calculate():
    exp = input("Please separate all numbers and operators with spaces. Write your expression below. Use numbers only\n ")
    digits = exp.split(' ')
    if len(digits) <3:
        return "This statement is invalid"
    while len(digits)>1:
        print(digits)
        while "*" in digits or "/" in digits:
            print(digits)
            if "*" in digits and "/" in digits:
                divide = digits.index("/")
                multiply = digits.index("*")
                if divide < multiply:
                    index = divide - 1
                else:
                    index = multiply - 1
            elif "*" in digits:
                index = digits.index("*") - 1
            elif "/" in digits:
                index = digits.index("/") - 1
            num = calculate(digits[index:index + 3])
            digits.pop(index)
            digits.pop(index)
            digits.pop(index)
            digits.insert(index, num)
        num = calculate(digits[0:3])
        digits.pop(0)
        digits.pop(0)
        digits.pop(0)
        digits.insert(0, num)
    return digits[0]

print(multi_calculate())