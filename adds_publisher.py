n=int(input('Number of streets->'))
rupees=12
total=0
for i in range(n):
    street=list(map(int,input().split()))
    count=1
    seen=street[0]
    for i in range(len(street)-1):
        if seen<street[i+1]:
            count=count+1
            seen=street[i+1]
    print(count*rupees)
    total=total+(count*rupees)
print(total)
