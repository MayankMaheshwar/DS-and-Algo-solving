import concurrent.futures
import time


def do(seconds):
    print("start sleeping")
    time.sleep(seconds)
    return 'done sleeping'+str(seconds)


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
