import math
import AI_LAB4

def Task1(x, y):
    a=math.exp(math.log(4)+math.log10(20))+math.pow(x,3)-5*y
    return a, math.round(a)

def Task2(x,y):
    a=(math.pow(8, x)-math.pow(y,2))
    b=math.sqrt(math.cos(math.radians(60)))
    c=(a*b)/math.sin(math.radians(30))
    return c, math.round(c)

