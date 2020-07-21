for _ in range(int(input())):
    n = int(input())
    a = list(input())
    b = list(input())
    res = []
    count = 0
    if a[0] != b[0]:
        count = 1
        res.append(1)
    for i in range(1,n):
        if a[i] != b[i]:
            res.append(i+1)
            res.append(1)
            res.append(i+1)
    print(len(res),' '.join(map(str,res)))