for _ in range(int(input())):
    a,b=map(int,input().split())
    a,b=max(a,b),2*min(a,b)
    print(max(a,b)**2)