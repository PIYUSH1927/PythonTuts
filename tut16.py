list1 = ["Harry", "Larry","carry","Marie"]
for item in list1:
    print(item)
 #this can be only be done in list , tuple,
list2= [["Harry" ,1 ],["Larry",2],["Carry",6],["Marie",250]]
for item , lollypop in list2:
    print(item,lollypop)
    #lly
for item , supply in list2:
    print(item,"and lolly is ",supply)
 #making dictionary
for item,supply in list2:#This line is not necessary for dictionary , written just for not mixing with above things,
    dict1=dict(list2)#dict() is making dictionary function
    print(dict1)
for item in dict1:
    print(item)
for item in dict1:
    print(dict1.items())
for item in dict1:
    print(dict1.keys())