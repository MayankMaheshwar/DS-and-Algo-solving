l=[[1,2],[1,4],[3,4]]
l.sort(key=lambda x:(x[0],-x[1]))
print(l)