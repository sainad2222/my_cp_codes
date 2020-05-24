for _ in range(int(input())):
    n=int(input())
    lis = list(map(int,input().split()))
    mi = 10000
    prev=10000
    lis.sort()
    for i in lis:
        mi = min(mi,abs(prev-i))
        prev = i
    print(mi)