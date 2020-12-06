def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
for _ in range(int(input())):
    n,k = map(int,input().split())
    points = []
    for i in range(n):
        x,y = map(int,input().split())
        points.append([x,y])
    ans = float('inf')
    for first in points:
        tmp = 1
        for second in points:
            if dist(first,second)>k:
                tmp = 0
        if tmp:
            print(1)
            break
    else:
        print(-1)

