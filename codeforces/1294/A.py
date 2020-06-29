for _ in range(int(input())):
    a,b,c,n=map(int,input().split())
    if (a+b+c+n)%3!=0:
        print("NO")
    else:
        x = (a+b+c+n)//3
        if a<=x and b<=x and c<=x:
            print("YES")
        else:
            print("NO")