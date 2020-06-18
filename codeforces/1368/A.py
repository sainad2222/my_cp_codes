for _ in range(int(input())):
    a,b,n=map(int,input().split())
    mi = min(a,b)
    ma = max(a,b)
    count = 0
    while(ma<=n):
        mi += ma
        ma,mi = max(ma,mi),min(ma,mi)
        count+=1
    print(count)