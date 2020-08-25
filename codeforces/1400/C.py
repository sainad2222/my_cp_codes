for _ in range(int(input())):
    s = input()
    x = int(input())
    n = len(s)
    w = ['1'] * n
    s2 = ['0'] * n
    for i in range(n):
        if s[i] == '0': 
            if i >= x:
                w[i - x] = '0'
            if i + x < n:
                w[i + x] = '0'
    for i in range(n):
        if i >= x and w[i - x] == '1':
            s2[i] = '1'
        if i + x < n and w[i + x] == '1':
            s2[i] = '1'
    print(''.join(w)) if(''.join(s2)==s) else print(-1)