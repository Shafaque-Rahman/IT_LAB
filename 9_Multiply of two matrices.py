x=[
   [2,1,2],
   [3,2,1],
   [1,2,3]
    ]
y=[
   [4,2,1],
   [2,1,3],
   [1,1,5]
    ]
r=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            r[i][j]+=x[i][k]*y[k][j]
[print(m) for m in tuple(r)]
