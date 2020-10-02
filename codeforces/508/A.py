# NTFS: nwi
n, m, k = map(int, input().split())
flag = 0
d = set()
for i in range(k):
    x, y = map(int, input().split())
    d.add((x, y))
    for j in [-1, 0]:
        for k in [-1, 0]:
            if all((x + j + a, y + k + b) in d for a in [0, 1] for b in [0, 1]):
                if not flag:
                    print(i + 1)
                flag = 1
if not flag:
    print(0)