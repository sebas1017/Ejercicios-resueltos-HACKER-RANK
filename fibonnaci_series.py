import time
start_time = time.time()


#numeros de fibonacci optimizacion
#solucion recursiva
def fib(x, y, upperLimit):
    return [x] + fib(y, (x+y), upperLimit) if x < upperLimit else [x]

#To test :

print(fib(0,1,10000000000000000000000000000000000000000000))
print("run time: " + str(time.time() - start_time))