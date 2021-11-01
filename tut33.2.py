x=90
def harry():
    x=20
    def rohan():
        global x
        x=33
        print(x)
    rohan()
    print(x)
harry()
print(x)