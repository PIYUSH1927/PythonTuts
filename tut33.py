l=10#Global variable
def fuction1(n):
    #l=5#local variable
    m=8
     global l
    l=l+45
    print(l,m)
    print(n)
fuction1("hello world")
print(l)