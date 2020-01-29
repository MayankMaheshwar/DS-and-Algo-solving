class demo:
    def __init__(self,name):
        self.name=name
        self.items=[]

    def add_items(self,name,price):
        item={"name":name,"price":price}
        self.items.append(item)

    def stock_price(self):
        total=0
        for i in self.items:
            total+=i["price"]
        return total
a=demo("bsnl")

a.add_items("bsnl",30)
a.add_items("airtel",40)
print(a.stock_price())

