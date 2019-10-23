n=int(input("Enter Nth number"))
for i in range(3,n+1):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
    if flag==0:
        print(i,end=" ")
       
