lis = list(map(int,input().split()))
nxt = 1
for i in lis:
    if i==0:
        print(nxt)
        break
    nxt+=1