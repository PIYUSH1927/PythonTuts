#Dictionary and its functions
d1={}
print(type(d1))
d2={"Harry":"Burger","Rohan":"fish","Shubham":{"B":"maggie","L":"Roti","D":"Chicken"}}
print(d2)
d2["Amkit"]=["Junk Food"]
d2["Aurangzeb"]=["kebabs"]
print(d2)
d2.update({"Leela":"Toffee"})#both this and above thing does the same work
[print(d2)]
del d2["Amkit"]
print(d2)
print(d2.keys())
print(d2.items())
print(d2["Harry"])
