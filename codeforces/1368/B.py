n = int(input())
lis = [1,1,1,1,1,1,1,1,1,1]
nxt = 0
prod = 1
def product(arr):
    prod = 1
    for i in arr:
        prod = prod*i
    return prod
while prod<n:
    lis[nxt]+=1
    nxt+=1
    nxt = nxt%10
    prod = product(lis)
s = 'codeforces'
for i in range(10):
    print(s[i]*lis[i],end="")