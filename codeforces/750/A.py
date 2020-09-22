n, k = map(int, input().split())
total = 4 * 60
k = total - k
tmp = n
c = 1
while tmp>0 and k>0:
    k -= c * 5
    if k < 0:
        break
    tmp -= 1
    c += 1
if tmp > 0:
    print(n - tmp)
else:
    print(n)