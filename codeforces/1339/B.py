t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    while(len(a) != 0):
        print(a.pop(len(a)//2), end=" ")
    print()