def mex(arr):
    tmp = [0] * 101
    for i in arr:
        tmp[i] = 1
    for i in range(102):
        if tmp[i] == 0:
            return i
    return 0
for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    A, B = [], []
    for i in lis:
        if i not in A:
            A.append(i)
        else:
            B.append(i)
    
    print(mex(A) + mex(B))
    continue