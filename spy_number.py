#spy number
n=132
add=0
mul=1
while n:
    r=n%10
    add=add+r
    mul=mul*r
    n=n//10
if add==mul:
    print('spy number')
else:
    print('not spy number')
    
