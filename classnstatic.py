class A(object):
    brothers=[]
    def __init__(self,name):
        self.name = name
a=A('r')
b=A('f')
a.brothers.append('s')
print(b.brothers)
