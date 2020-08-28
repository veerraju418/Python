#lucky array 
arr=[1,2,3,4,1,2,3,1]
count=0
min_val=arr[0]
for i in arr:
    if i<min_val:
        min_val=i
for i in arr:
    if min_val==i:
        count+=1
if count%2!=0:
    print('Lucky array')
else:
    print('Unlucky array')
