n1=int(input('enter n1'))
n2=int(input('enter n2'))
while True:
    if n1>n2:
        n1,n2=n2,n1
        n2=n2%n1
        if n2==0:
            break
    else:
        n2=n2%n1
        if n2==0:
            break
print('GCD=',n1)
