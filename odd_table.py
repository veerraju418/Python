n=int(input('enter table'))
r=int(input('enter range'))
for i in range(1,r+1):
    if i%2==0:
        continue
    else:
        print(n,'X',i,n*i)
        
