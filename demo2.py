def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def calculator(a,b,op):
    if op=='+':
        return add(a,b)
    elif op=='-':
        return sub(a,b)
    elif op=='*':
        return mul(a,b)
    elif op=='/':
        return div(a,b)
    else:
        return "Invalid operator"
while True:
        a=float(input("Enter first number: "))
        op=input("Enter operator (+,-,*,/): ")
        b=float(input("Enter second number: "))
        result=calculator(a,b,op)
        print("Result: ",result)
#简单计算器