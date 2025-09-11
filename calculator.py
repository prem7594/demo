#Create a calculator
first=int(input("enter first number"))
operator=(input("enter operator (+,-,*,%)"))
second=int(input("enter second number"))
if operator == '+':
    print("Result:", first + second)
elif operator == '-':
    print("Result:", first - second)
elif operator == '*':
    print("Result:", first * second)
elif operator == '%':
    print("result;",first % second)