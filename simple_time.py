import time

def procedure():
    time.sleep(2.5)
t0 = time.process_time()
procedure()
t1 = time.process_time()

elapsed_time = (t1-t0)/1000

print("t0 = ",t0)
print("t1 - ",t1)
print("Elapsed time =",elapsed_time)
t2 = time.time()
procedure()
t3 = time.time()
print("time t2",t2)
procedure()
print("time t3",t3)

elapsed_time2 = t3-t2
print("elapsed time 2",elapsed_time2)

