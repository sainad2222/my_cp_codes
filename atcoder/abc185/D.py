def ceil(a, b):
    return (a + b - 1) // b
n,m = map(int,input().split())
if m==0:
    print(1)
    exit()
lis = list(map(int,input().split()))
lis.sort()
arr = []
prev = 0
for i,elem in enumerate(lis):
    if elem-prev-1 == 0:
        prev = elem
        continue
    arr.append(elem - prev - 1)
    prev = elem
if n-prev!=0:
    arr.append(n - prev)
if not arr:
    print(0)
    exit()
ans = 0
mi = min(arr)
for i in arr:
    ans += ceil(i,mi)
print(ans)
