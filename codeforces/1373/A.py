for _ in range(int(input())):
    a,b,c=map(int,input().split())
    # for first case
    first,second = 0,0
    if c<=a:
        first = -1
    else:
        first = 1
    # for second case
    if c/b>=a:
        second = -1
    else:
        second = b
    print(first,second)