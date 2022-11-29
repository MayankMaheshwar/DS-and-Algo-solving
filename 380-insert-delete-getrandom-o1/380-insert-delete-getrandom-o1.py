import random
class RandomizedSet:

    def __init__(self):
        self.l,self.pos=[],{}
        

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.l.append(val)
            self.pos[val]=len(self.l)-1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        
        if val in self.pos:
            if len(self.l)==1 or val==self.l[-1]:
                self.l.pop()
                del self.pos[val]
            else:    
                idx = self.pos[val]
                v=self.l.pop()
                self.l[idx] = v
                del self.pos[val]
                self.pos[v]=idx
               
            return True
        return False

    def getRandom(self) -> int:
        return self.l[random.randint(0, len(self.l) - 1)]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()