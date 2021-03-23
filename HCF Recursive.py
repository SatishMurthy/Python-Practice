from timeit import default_timer as timer

def compute_hcf(n1,n2):
    if(n2==0):
        return n1
    else:
        return compute_hcf(n2,n1%n2)

# num1 = 542344223234324324342324
# num2 = 243432344

num2 = 542344223234324324342324
num1 = 243432344

# num1=5423421342225
# num2=2425


start = timer()

print("The H.C.F. is", compute_hcf(num1, num2))

end = timer()
print("Execution Time = ",end - start," seconds") # Time in seconds, e.g. 5.38091952400282