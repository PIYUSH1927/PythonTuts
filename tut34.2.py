i=0
def greet():
    global i
    i=i+1
    print("hello",i)
    greet()
greet()
