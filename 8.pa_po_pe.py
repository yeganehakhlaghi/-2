import random

while 'true':
    comp1=random.randint(1,2)
    comp2=random.randint(1,2)
    #1-> ✋  2-> 🤚    
    print("Chose one:")
    print("1-> ✋")
    print("2-> 🤚")
    print("exit")
    user = int(input())
    #print("comp1",comp1)
    #print("comp2",comp2)
    if(comp1 == comp2):
        if comp1==user:
            if user==1:
                print("Everyone has chosen ✋")
                print("No one won")
            elif user==2:
                print("Everyone has chosen 🤚")
                print("No one won")
        elif comp1!=user:
            if user==1:
                print("You has chosen ✋")
                print("The computer1 has chosen 🤚")
                print("The computer2 has chosen 🤚")
                print("You won")
            elif user==2:
                print("You has chosen 🤚")
                print("The computer1 has chosen ✋")
                print("The computer2 has chosen ✋")
                print("You won")

    if(comp1 == user):
        if comp1==comp2:
            if comp2==1:
                    print("Everyone has chosen ✋")
                    print("No one won")
            elif comp2==2:
                    print("Everyone has chosen 🤚")
                    print("No one won")
        elif comp1!=comp2:
            if user==1:
                    print("You has chosen ✋")
                    print("The computer1 has chosen ✋")
                    print("The computer2 has chosen 🤚")
                    print("computer2 won")
            elif user==2:
                    print("You has chosen 🤚")
                    print("The computer1 has chosen 🤚")
                    print("The computer2 has chosen ✋")
                    print("computer2 won")
    if(comp2 == user):
        if comp1==comp2:
            if comp1==1:
                    print("Everyone has chosen ✋")
                    print("No one won")
            elif comp1==2:
                    print("Everyone has chosen 🤚")
                    print("No one won")
        elif comp1!=comp2:
            if user==1:
                    print("You has chosen ✋")
                    print("The computer1 has chosen 🤚")
                    print("The computer2 has chosen ✋")
                    print("computer2 won")
            elif user==2:
                    print("You has chosen 🤚")
                    print("The computer1 has chosen ✋")
                    print("The computer2 has chosen 🤚")
                    print("computer2 won")
        elif user=='exit':
            break
        else:
            print("is not true!!")






