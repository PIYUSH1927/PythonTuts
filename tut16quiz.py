#Quiz
#Make a list of number and words , detect whether it is number or not & if it is a number
#then check if it is greater than and equal to 7 or not & if greater than or equal to 7 then print the number.
#if less than 7 print lesser
#if not a number print non numeric

list=["harry", "25" , "manny" , "zebra","4" , "89" , "08" , "sunny","3","7"]
for item in list:
    if str(item).isnumeric() and int(item) >= 7 :
        print(item)
    elif str(item).isnumeric() and int(item)<7:
        print("lesser")
    else:
        print("non numeric")

#Here we used for loop function with if else fuction.
