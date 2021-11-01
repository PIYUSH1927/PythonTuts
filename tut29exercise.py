#Exercise 4 --- Question in diary
n=int(input("Enter a number between 1 to 10 \n "))
m=int(input("choose a number between 0 or 1\n"))
if bool(m):
    for i in range(1,n+1,1):
        print("*"* int(i))
else:
    for i in range (n+1,1,-1):
        print("*"* int(i))
