for _ in range(int(input())):
    x, y = map(int, input().split())
    if abs(x - y) > 1:
        print(2*abs(x-y)-1+2*min(x,y))
    else:
        print(x+y)