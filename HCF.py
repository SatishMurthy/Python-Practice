from timeit import default_timer as timer

def compute_hcf(x, y):
# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

# num1 = 542344223234324324342324
# num2 = 243432344
#
num1=5423421342225
num2=2425

start = timer()

print("The H.C.F. is", compute_hcf(num1, num2))

end = timer()
print("Execution Time = ",end - start," seconds") # Time in seconds, e.g. 5.38091952400282