#Quiz       #Ask a person his age & if he is above 18 print you are eligibel to drive
#if below 18 print you are not eligible to drive.
#if age is above 18 print please enter a valid age.
#if equal to 18 print you have to come to office to check whether you are eligible or not.
print("Enter your age ")
age = int(input())

if 110>age>18:
    print("you are eligible to drive.")
elif age==18:
    print("you have to come to office to check whether you are eligible to drive or not.")
elif age>110:
    print("please enter a valid age ")
else:
    print("you are not eligible to drive.")