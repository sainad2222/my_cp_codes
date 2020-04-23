for i in range(int(input())):
    n,a,b,c,d = map(int,input().split())
    low = a-b
    high = a+b
    glow = c-d
    ghigh = c+d
    if(n*low>ghigh or n*high<glow):
        print("No")
    else:
        print("Yes")