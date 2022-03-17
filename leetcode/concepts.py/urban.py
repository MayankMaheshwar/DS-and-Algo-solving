from collections import defaultdict
items = [("Biryani", "Chicken Biryani"), ("Biryani", "Veg Biryani"),
         ("Curries", "Chicken Curry"), ("Curries", "Veg Curry")]

dic = defaultdict(list)

for k, v in items:
    dic[k].append(v)

print(dic)
