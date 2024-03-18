import math

def TaylorSinus(x,n):
    
    result=0.

    for i in range(n):
        result+=((math.pow(-1, i))*math.pow(x,2*i+1))/math.factorial(2*i+1)

    return result

def TaylorCosinus(x,n):
    result=0.

    for i in range(n):
        result+=(math.pow(-1,i)*math.pow(x,2*i))/math.factorial(2*i)

