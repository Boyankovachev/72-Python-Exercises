#Please write a program to print the running time of execution of "1+1" for 100 times.


import timeit
time = timeit.Timer("for i in range(200):1+1")
print(time.timeit())