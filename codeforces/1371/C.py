for _ in range(int(input())):
    a,b,n,m=map(int,input().split())
    if(a+b<n+m):
        print("No")
        continue
    elif min(a,b)<m:
        print("No")
        continue
    


    print("Yes")