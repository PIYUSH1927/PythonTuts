n1=input("enter first number")
n2=input("enter second number")
try:
    print(int(n1)+int(n2))
except Exception as z:
    print(z)
#now even if any error comes in above program further program will continue
print(int(n1)+3)

