# IGiveUp
## NTFS: ranjithm2001
n = int(input())
lis = list(map(int, input().split()))
if lis == sorted(lis):
    print(0)
else:
    for i in range(1, n):
        if lis[i] < lis[i - 1]:
            tmp = lis[i:] + lis[:i]
            if sorted(tmp) == tmp:
                print(n - i)
            else:
                print(-1)
            break