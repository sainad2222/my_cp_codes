for _ in range(int(input())):
    x,y,n=map(int,input().split())
    if x>n:
        print(y)
        continue
    rem = n%x
    if rem<y:
        n-=x
    print(n+y-rem)