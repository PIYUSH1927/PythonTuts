#Writing and appending a file
f=open("tut28.txt","w")
f.write("this is result part of tut 28.py\n")
f.close()

f=open("tut28.txt","a")#here a means append - joining anything in the existing file
f.write("ignore txt files\n")
f.close()

#To find number of characters witten in file in append mode
f=open("tut28.txt","a")
a=f.write("ignore txt files\n")
print(a)
f.close()

#To find number of characters witten in file in write mode
"""f=open("tut28.txt","w")
a=f.write("this is result part of tut 28.py\n")
print(a)
f.close()"""

#To open a file for both read and write
f=open("tut28.txt","r+")
print(f.read())
f.write("  thank you")