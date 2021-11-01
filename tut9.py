#Python list and list fuctions
numbers=[2,4,9,7,6]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers[0:5])
print(numbers[::2])
print(max(numbers))
numbers.append(66)
print(numbers)
numbers.insert(2,67)
print(numbers)
numbers.remove(7)
print(numbers)
numbers.pop()
print(numbers)
numbers[1]=98
print(numbers)
tp=(2,4,6,8)#this is a tuple & in tuple we cant exchange the value like we did before this question
#we identify a tuple by () this bracket as ,in list we use square[] brackets.

#swapping two numbers
a=2
b=6
a,b=b,a
print(a,b)
