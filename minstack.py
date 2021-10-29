class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack= []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:self.stack.append((x,x)) 
        else:
            self.stack.append((x,min(x,self.stack[-1][1])))

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack: self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack: return self.stack[-1][0]
        else: return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack: return self.stack[-1][1]
        else: return None





class MinStack:

def __init__(self):
    self.q = []

# @param x, an integer
# @return an integer
def push(self, x):
    curMin = self.getMin()
    if curMin == None or x < curMin:
        curMin = x
    self.q.append((x, curMin))

# @return nothing
def pop(self):
    self.q.pop()


# @return an integer
def top(self):
    if len(self.q) == 0:
        return None
    else:
        return self.q[len(self.q) - 1][0]


# @return an integer
def getMin(self):
    if len(self.q) == 0:
        return None
    else:
        return self.q[len(self.q) - 1][1]