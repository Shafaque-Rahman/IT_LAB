
n=int(input("Enter no of series"))
a=0
b=1
print(f"{a}, {b} ",end=', ')
for i in range(1,n+1):
    sum=a+b
    print(sum,end=', ')
    a=b
    b=sum
