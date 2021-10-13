import math

while "true":
    print("Select an operation:")
    print("+")
    print("-")
    print("*")
    print("/")
    print("sin")
    print("cos")
    print("tan")
    print("cot")
    print("log")
    print("exit")

    op=input()

    if op=='+':
        num1=int(input())
        num2=int(input())
        res=num1+num2

    elif op=='-':
        num1=int(input())
        num2=int(input())
        res=num1-num2

    elif op=='*':
        num1=int(input())
        num2=int(input())
        res=num1*num2

    elif op=='/':
        num1=int(input())
        num2=int(input())
        if num2==0:
            print("Cannot be divided by 0")
        else :
            res=num1/num2

    elif op=='sin':
        num1=int(input())
        res=math.sin(num1)

    elif op=='cos':
        num1=int(input())
        res=math.cos(num1)

    elif op=='tan':
        num1=int(input())
        res=math.tan(num1)

    elif op=='cot':
        num1=int(input())
        res=math.sin(num1)
        
    elif op=='log':
        num1=int(input())
        res=math.log(num1)

    elif op=='exit':
        break

    else:
        res=("Selected operation is not true")
    
    print("result = ",res)

