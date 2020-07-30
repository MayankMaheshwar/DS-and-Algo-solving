class Graph:
    def __init__(self):
       self.dic={}
    def addVertex(self,node):
        self.dic[node]=set()
    
    def addEdge(self,node1,node2):
        self.dic[node1].add(node2)    
        self.dic[node2].add(node1)

mayank=Graph()
mayank.addVertex("maya")
mayank.addVertex("may")
mayank.addVertex("ma")
mayank.addVertex("mahesh")
mayank.addEdge("may","mahesh")
mayank.addEdge("may","ma")
mayank.addEdge("mahesh","ma")
mayank.addEdge("maya","mahesh")

print(mayank.dic)        