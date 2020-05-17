import math
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if(b>=a):
        print(b)
    else:
        if(d>=c):
            print(-1)
            continue
        rem=math.ceil((a-b)/(c-d))
        print(b+rem*c)