n = int(input())
lis = list(map(int, input().split()))
lis = [0] + lis
for i in range(1, n + 1):
    if lis[lis[lis[i]]] == i:
        print("YES")
        break
else:
    print("NO")