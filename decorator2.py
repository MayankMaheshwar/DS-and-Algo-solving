import time

def time_it(func):
    def wrapper(*args,**kwargs):
        
        start=time.time()
        res=func(*args,**kwargs)
        end=time.time()
        print(func.__name__+" took ", (end-start)*1000 , "mil_sec")
        return res
    return wrapper

    
@time_it
def square(numbers):
    #start=time.time()
    res=[]
    for num in numbers:
        res.append(num*num)
    #end=time.time()
    #print("time take", (end-start)*1000)
    return res    

@time_it
def cube(numbers):
    #start=time.time()
    res=[]
    for num in numbers:
        res.append(num*num*num)
    #end=time.time()   
    #print("time take", (end-start)*1000) 
    return res    

array=range(1,100000)
sq= square(array)
cb=cube(array)