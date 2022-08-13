import random
choice=input("enter play or exit: ")
while(choice=="play"):
    u=input("enter your choice either rock, paper or scissor: ")
    if(u!='rock' and u!='Rock' and u!='ROCK' and u!='paper'and u!='Paper' and u!='PAPER' and u!='scissor'and u!='Scissor' and u!='SCISSOR'):
        print("invalid input")
        
    else:
        v=random.randint(1,3)
        if(v==1):
            print("Computer's move: Rock")
        if(v==2):
            print("Computer's move: Paper")
        if(v==3):
            print("Computer's move: Scissors")
        if(u=='rock' or u=='Rock' or u=='ROCK'):
            t=1
        if(u=='paper'or u=='Paper' or u=='PAPER'):
            t=2
        if(u=='scissor'or u=='Scissor' or u=='SCISSOR'):
            t=3
        if(t==v):
            print("you and computer had a tie. Try again!")
        elif(t==1):
            if(v==2):
                print("You Lost. Try again!")
            else:
                print("Congratulations! You Won.")
        elif(t==2):
            if(v==3):
                print("You Lost. Try again!")
            else:
                print("Congratulations! You Won.")
        else:
            if(v==1):
                print("You Lost. Try again!")
            else:
                print("Congratulations! You Won.")
    choice=input("enter play or exit: ")
    if(choice=="exit"):
        print("you left the game!")
        break;
#C:\Users\user\Videos\Captures