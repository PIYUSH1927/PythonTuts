#Exercise2 (faulty calculator)
#faults (453 * 3 =555 , 56+9=67, 56/6=4)
print("Enter your first number")
n1=int(input())
print("Enter your second number")
n2=int(input())
print("choose operation (+,-,*,/)")
n3=input()
if n1==453 and n2== 3 and n3=="*":
    print("555")
elif n1==56 and n2== 9 and n3=="+":
    print("67")
elif n1==56 and n2==6 and n3=="/":
    print("4")
elif n3=="+":
    print((n1) + (n2))
elif n3=="-":
    print ((n1) - (n2))
elif n3=="*":
    print((n1) * (n2))
else:
    print((n1) / (n2))


