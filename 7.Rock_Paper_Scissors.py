import random
while 'true':
    comp=random.randint(1,3)
    #1 -> R  2-> p   3-> S
    print("Choose one :")
    print(" S for Scissors ")
    print(" P for Paper ")
    print(" R for Rock ")
    print(" exit")
    user = input()
    if user == 'S':
        print("your selection ✌")
        if comp == 1:
            print("Computer selection ✊")
            print("The computer won")
        elif comp == 2:
            print("Computer selection ✋")
            print("You won")
        elif comp == 3:
            print("Computer selection ✌")
            print("You were equal")


    elif user == 'P':
        print("Your selection ✋")
        if comp == 1:
            print("Computer selection ✊")
            print("You won")
        elif comp == 2:
            print("Computer selection ✋")
            print("You were equal")
        elif comp == 3:
            print("Computer selection ✌")
            print("The computer won")

    elif user == 'R':
        print("your selection ✊")
        if comp == 1:
            print("Computer selection ✊")
            print("You were equal")
        elif comp == 2:
            print("Computer selection ✋")
            print("The computer won")
        elif comp == 3:
            print("Computer selection ✌")
            print("You won")
    elif user=='exit':
        break
    else:
        print("is not true!!")



