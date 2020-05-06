for _ in range(int(input())):
    n,m=map(int,input().split())
    flag=0
    if(n==1 or m==1):
        flag=1
    elif(n==2 and m==2):
        flag=1
    print("YES") if(flag) else print("NO")