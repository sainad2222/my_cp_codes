# NTFS: belkka
n, k = map(int, input().split())
lis = list(map(int, input().split()))
if k >= n - 1:
    print(n)
else:
    best = 0
    cur = None
    for elem in lis:
        if elem > best:
            best = elem
            if cur is not None:
                cur = 1
            else:
                cur = 0
        else:
            cur += 1

        if cur == k:
            print(best)
            break
    else:
        print(best)
