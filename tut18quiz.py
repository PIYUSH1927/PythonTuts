#Quiz# Write a program which take input from the user till it is greater than hundred
# and if the given input is greater than 100 print congratulations you have printed number greater than hundred else print try again.
while(True):
    i=int(input("Enter a number "))
    if i > 100:
         print("congratulations you have printed number greater than hundred")
    else:
        print("try again")
        continue
#here if we will give continue first and break later then
#after once typing a nummber greater than 100 the program will not take more input
#here we can give as many input as we want as it is ended with continue so the program never ends
#thats why here we dont use break



