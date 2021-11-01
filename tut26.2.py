f= open ("tut26.txt")
content= f.read()
print(content)
f.close()

f=open("tut26.txt" , "rb")
content=f.read()
print(content)
f.close()

f=open("tut26.txt")
content=f.read(3)
print(content)

content=f.read(4)
print(content)
f.close()#important to close

f= open ("tut26.txt")
for line in f:
    print(line)

f = open("tut26.txt")
print(f.readline())
print(f.readline())

f = open("tut26.txt")
print(f.readlines())   
