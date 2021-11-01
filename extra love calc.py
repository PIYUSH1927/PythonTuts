#Love Calculator
print("Welcome to the love calculator")
print()
n1=input("Enter your name\n")
n1=n1.lower()
n2=input("Enter your partner name\n")
n2=n2.lower()
n3=n1+n2
x1=n3.count("t")
x2=n3.count("r")
x3=n3.count("u")
x4=n3.count("e")
x=x1+x2+x3+x4
y1=n3.count("l")
y2=n3.count("o")
y3=n3.count("v")
y4=n3.count("e")
y=y1+y2+y3+y3
percent = x*10 + y
if int(percent) >= 90 or int(percent) <= 10 :
    print("You go together like coke and mentos")
elif int(percent) >= 40 and int(percent)<= 50:
    print("You are alright")
else:
    print(f"Your score is {percent} out of 100")


