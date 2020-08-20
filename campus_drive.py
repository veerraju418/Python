#TCS reqruitment
lst=list()
while True:
    
    name=input('Name-->')
    if name=='done':
        break
    rollno=input('id---->')
    college=input('college--->')
    branch=input('Branch--->')
    yof=int(input('Year Of Study-->'))
    backlog=int(input('no of backlogs-->'))
    if college=='Aditya Engineering College' and (branch=='CSE' or branch=='IT' or branch=='ECE')and yof==3 and backlog==0:
        print('Eligible for campus drive')
        lst.append(rollno)
    
    else:
        print('Not Eligible for campus drive')
print('Candidates Who are eligible for TCS campus drive')
print(lst)
