a,b=map(int,input().split())
a1=a
b1=b
r=2
sum=1
while True:
    if a%r==0 and b%r==0:
        a=a//r
        b=b//r
        sum=sum*r
    else:
        r+=1
    if a<r or b<r:
        break
lcm=sum*a*b
print('LCM of',a1,'and',b1,'is',lcm)
