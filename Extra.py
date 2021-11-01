#PYTHON PIZZA Billing Counter
print("Welcome to Python Pizza\nwhich pizza you would like to have\nSmall pizza:$15 ,Medium Pizza:$20 ,Large Pizza:$25")
n1=input("Press 'S' for small, 'L' for large , 'M' for medium\n")
n1=n1.capitalize()
n2=input("Would you like to have Pepperoni\nsmall pizza: $2\nmedium and large pizza: $3\nPress 'Y' for yes and 'N' for no \n")
n2=n2.capitalize()
n3=input("Would you like to have extra cheese?\nExtra cheese for any size pizza costs $1\nPress 'Y' for yes and 'N' for no\n")
n3=n3.capitalize()
if n1=="S" and n2=="Y"and n3=="Y":
    print("Your total cost is $18")
elif n1=="S" and n2=="Y" and n3=="N":
    print("Your total cost is $17")
elif n1=="S" and n2=="N" and n3=="Y":
    print("Your total cost is $16")
elif n1=="M" and n2=="Y" and n3=="Y":
    print("Your total cost is $24")
elif n1=="M" and n2=="Y" and n3=="N":
    print("Your total cost is $23")
elif n1=="M" and n2=="N" and n3=="Y":
    print("Your total cost is $21")
elif n1=="L" and n2=="Y" and n3=="Y":
    print("Your total cost is $29")
elif n1=="L" and n2 == "Y" and n3=="N":
    print("Your total cost is $28")
elif n1=="L" and n2=="N" and n3=="Y":
    print("Your total cost is $26")

print("Thank you, Have a great day")


