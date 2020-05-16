for _ in range(int(input())):
    n,k=map(int,input().split())
    k-=1
    while(k!=0):
        ma=-1;mi=11
        temp=n
        while(temp>0):
            r=temp%10
            ma=max(r,ma)
            mi=min(r,mi)
            temp=temp//10
        if(mi==0):
            break
        n+=ma*mi
        k-=1
    print(n)