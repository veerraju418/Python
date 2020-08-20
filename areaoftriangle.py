#area of triangle
import math as m
a,b,c=map(int,input().split(' '))
s=(a+b+c)/2
area=m.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
