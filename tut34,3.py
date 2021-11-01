def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
v=fact(7)
print(v)