s = set()
print(type(s))
l=[1,2,3,4,5]
s2 = set(l)
print(s2)
#now adding elemets in blank set s
s.add(1)
s.add(2)
print(s)#=> s={1,2}
s1 = s.union({1,2,3})
print(s1)
print(s,s1)
s3 = s.intersection({1,2,3})
print(s,s1,s3)
print(len(s))
print(max(s1))#lly for maximum
s4={4,5}
print(s1.isdisjoint(s4))#disjoint set are sets in which there are no elements in common
s.remove(2)
print(s)