n=12345
p=0
while n!=0:
    r=n%10
    count=0
    for i in range(1,r+1):
        if r%i==0:
            count=count+1
    if count==2:
        p=p+1
    n=n//10   
print(p)
            
