import _thread
import time


def cir(thread1):
    cd = 10
    while cd > 0:
        print(cd, A)
        cd -= 1
        time.sleep(2)


try:
    _thread.start_new_thread(cir, ("thread1",))
except:
    print("NA")
while 1:
    pass
