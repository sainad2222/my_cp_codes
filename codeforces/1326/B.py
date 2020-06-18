n = int(input())
b = list(map(int,input().split()))
a = [0]*n
a[0]=b[0]
prev = a[0]
for i in range(1,n):
    a[i]=b[i]+prev
    prev = max(prev,a[i])
print(' '.join(map(str,a)))