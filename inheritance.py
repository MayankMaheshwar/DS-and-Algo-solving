class Mom:
        def __init__(self,name,color):
                self.name=name
                self.color=color
        def lov(self):
                print("hello " + self.name)
        def __add__(self,other):
                return Mom(self.name+ other.name,self.color+ other.color)                



class Mayank(Mom):
        def love(self):
                print("love u mom")
                super().lov()


m=Mayank("Mom","nm")
print(m.name)
m.love()

first=Mom("Mayank ","Love")
second=Mom("Maheshwari"," U mom")
result=first+second
print(result.name)
print(result.color)
