h, w = map(int, input().split())
matrix = []
mi = float('inf')
for i in range(h):
    tmp = list(map(int, input().split()))
    mi = min(mi, min(tmp))
    matrix.append(tmp)
ans = 0
for i in range(h):
    for j in range(w):
        ans += abs(mi - matrix[i][j])
print(ans)
