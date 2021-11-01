class employee:
    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary

    def details(self):
        print(self.salary, self.name)


harry=employee("harry",455)
rohan=employee("rohan",566)



harry.details()
print(rohan.salary)

#print(harry.salary)
#print(rohan.name)
