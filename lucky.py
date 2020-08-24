n=341
temp=n
d_c=0
count=0
#check number is divisible by individual numbers
while True:
    if n==0:
        break
    r=n%10
    if temp%r==0:
        d_c+=1
    count+=1
    n=n//10
    
if count==d_c:
    print('Lucky number')
else:
    print('Unlucky number')
        
