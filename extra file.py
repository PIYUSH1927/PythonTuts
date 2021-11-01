n1=input("choose Heads or Tails \n")
n1=n1.capitalize()
import random
x=random.randint(0,2)
if n1=="Heads" and x==1:
    print("Congratulations, you won the toss ")
elif n1=="Tails" and x==0:
    print("Congratulations,you won the toss")
else:
    print("You lost the toss")

