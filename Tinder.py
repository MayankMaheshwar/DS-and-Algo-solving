#class creation
class user:
    def __init__(self,name,age,sex,city):
        # taking the necessary details(revelance to your project) and avoiding the rest (abstraction)
        self.name = name
        self.age = age
        self.sex = sex

#inheritance
class male(user):
    pass
#inheritance
class female(user):
    pass
#inheritance
class other(user):
    pass




#object creation
a = male('mayank',15,"M","raebareli")
print(a.name)





