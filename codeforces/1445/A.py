t = int(input())
for T in range(t):
    n, x = map(int, input().split())
    lis1 = list(map(int, input().split()))
    lis2 = list(map(int, input().split()))
    lis2 = sorted(lis2, reverse=True)
    for i, j in zip(lis1, lis2):
        if i + j > x:
            print("No")
            if T != t - 1:
                input()
            break
    else:
        print("Yes")
        if T != t - 1:
            input()