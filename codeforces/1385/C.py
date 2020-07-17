# NTFS: pajenegod
for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    lis.reverse()
    i = 1
    while i<n and lis[i-1]<=lis[i]:
        i+=1
    while i<n and lis[i-1]>=lis[i]:
        i+=1
    print(n-i)