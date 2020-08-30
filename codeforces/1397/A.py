for _ in range(int(input())):
    n = int(input())
    strs = {}
    for i in range(n):
        s = input()
        for j in s:
            if j not in strs:
                strs[j] = 1
            else:
                strs[j] += 1
    lis = list(strs.values())
    flag = 1
    for i in lis:
        if i % n != 0:
            flag = 0
            break
    print("YES") if flag else print("NO")