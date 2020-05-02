for _ in range(int(input())):
    n = int(input())
    sum1,sum2=0,0
    lis=[pow(2,x) for x in range(1,n+1)]
    sum1=lis[-1]
    for i in range(0,n//2-1):
        sum1+=lis[i]
    for i in range(n//2-1,n-1):
        sum2+=lis[i]
    print(abs(sum1-sum2))