for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    sum = 0
    i=0
    while(i>=0 and i<n):
        j = i
        cur = lis[i]
        while(j<n and abs(lis[i]+lis[j])==abs(lis[i])+abs(lis[j])):
            cur = max(cur,lis[j])
            j+=1
        sum += cur
        i = j
    print(sum)