for _ in range(int(input())):
    n = int(input())
    s = input()
    a, b = '1', '1'
    flag = 0
    for i in range(1, n):
        if not flag:
            if s[i] == '1':
                a += '1'
                b += '0'
                flag = 1
            elif s[i] == '2':
                a += '1'
                b += '1'
            else:
                a += '0'
                b += '0'
        else:
            if s[i] == '1':
                a += '0'
                b += '1'
            elif s[i] == '2':
                a += '0'
                b += '2'
            else:
                a += '0'
                b += '0'
    print(a)
    print(b)
