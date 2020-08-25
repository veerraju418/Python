#strong number
n=145#1+24+120=145
temp=n
sum=0
while n:
    r=n%10
    fc=1
    for i in range(1,r+1):
        fc=fc*i
    sum=sum+fc
    n=n//10
if temp==sum:
    print('strong number')
else:
    print('not strong number')

