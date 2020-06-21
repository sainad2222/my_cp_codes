n = int(input())
lis = list(map(int,input().split()))
X = lis[0]
for i in range(1,n):
    X ^= lis[i]
for i in lis:
    print(X^i,end=" ")