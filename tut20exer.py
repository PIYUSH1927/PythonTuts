#Exercise
#Keep any number between 1 to 99 and say user to guess the number
#if user guesses a number greater than that number print your number is greaater than than the correct number and vice versa for smaller number
#if the user takes more than 10 chances print game over and if the user guesses the correct number print you won.
n=45
i=0
print("Total chances = 5")
while (i < 5 ):
    i=i+1


    n1=int(input("Guess a number between 1 to 99 \n"))

    if n1 > n :
        print("entered number is greater than the correct number,",5-i,"attempts left")
    elif (n1) < n:
        print("entered number is smaller than the correct number,",5-i,"attempts left")
        continue
    elif (n)==45:
        print("You Won")
        break
if i >= 5:
    print("Game over")
    print("Correct number was 45")







