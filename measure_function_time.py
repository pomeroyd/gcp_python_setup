import time

# for 16, it takes 2.5 seconds on Google E2 medium 2cpu
# for 16 it takes 20 seconds on my laptop


print("starting program")

#for a value x sum the values in the tuple


t2 = time.time()
print("t2 = ",t2)
my_tuple = range(10)

def count(x):
    sum = 0
    for x in my_tuple:
        sum = sum+x
        print("sum = ",sum)
    return sum

increment = 1
final_sum = 0
while(final_sum<2**16):
    my_tuple = range(increment)
    final_sum = count(my_tuple)
    print("final sum = ",final_sum)
    increment+=1




t3 = time.time()
print("time t3",t3)

elapsed_time2 = t3-t2
print("elapsed time 2",elapsed_time2)

