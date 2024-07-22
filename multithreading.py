import threading
import time
def fun(sec):
    print(f"Total {sec} required...\n")
    time.sleep(sec)
    return sec


start=time.perf_counter()
#normal code
fun(4)
fun(2)
fun(7)
end=time.perf_counter()
print(f"Time required for norml code running is : {end-start} seconds\n")

start=time.perf_counter()
#using multitreading
t1=threading.Thread(target=fun,args=[4])
t2=threading.Thread(target=fun,args=[2])
t3=threading.Thread(target=fun,args=[7])

t1.start()
t2.start()
t3.start()
#wait for finising all t1,t2,t3 task
t1.join()
t2.join()
t3.join()
end=time.perf_counter()
print(f"Time required for multitreading is : {end-start} seconds\n")

from concurrent.futures import ThreadPoolExecutor
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        l=[1,2,3,4,5]
        results=executor.map(fun,l)
        for result in results:
            print(result)
poolingDemo()