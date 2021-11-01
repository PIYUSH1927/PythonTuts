#Game Development : Snake water gun
print("Welcome to the game of snake water gun\n you have 10 rounds of play")
print()
your_points=0
computer_points=0
import random


i=0
while(i<10):
    i=i+1
    y1 = input("type S to select snake and W , G for water and gun respectively \n ")
    y1 = y1.capitalize()

    x=random.choice("S W G")

    if y1=="S" and x=="W" :
        print("you won ")
        your_points+=1
        print()

    elif y1=="W" and x=="G":
        print("you won ")
        your_points+=1
        print()
    elif y1=="G" and x=="S":
        print("you won ")
        your_points+=1
        print()
    elif y1==x:
        print("draw")
        print()
    else:
        print("you lose")
        computer_points+=1
        print()
print("10 rounds over")
print("your points = ",your_points)
print("computer points =",computer_points)
if your_points > computer_points:
    print("You Won the game")
elif your_points == computer_points:
    print("Game Draw")
else:
    print("You lose computer won")


