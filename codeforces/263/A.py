lis=[]
for i in range(5):
    temp = list(map(int,input().split()))
    lis.append(temp)
for i in range(5):
    for j in range(5):
        if(lis[i][j]==1):
            res=[i,j]
print(abs(res[0]-2)+abs(res[1]-2))