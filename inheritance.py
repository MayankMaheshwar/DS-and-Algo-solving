class animal:
        def __init__(self, dogname):
                self.name= dogname

        def define(self):
                print("my name is dog") 

        def eat(self,food):
                print("i eat"+ food)

class dog(animal):
        def eat(self,food):
                print("i eat"  + food)

d=dog("mike")
d.define()
animal.eat
