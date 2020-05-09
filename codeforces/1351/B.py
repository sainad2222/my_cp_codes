for _ in range(int(input())):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    if((b==c and a+d==b) or (a==d and b+c ==d) or(a==c and b+d==a) or (b==d and a+c==b)):
        print("Yes")
    else:
        print("No")