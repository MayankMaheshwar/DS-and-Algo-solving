# You have a function rand7() that generates a random integer from 1 to 7. Use it to write a function rand5() that generates a random integer from 1 to 5.
import random
def rand7():
    return random.randrange(0,7)
def rand5():
    result=7
    while result>5:
        result=rand7()
    return result
if __name__=="__main__":

    print(random.random())
    print(rand7())        