for _ in range(int(input())):
    n = int(input())
    st = '0123456789'
    if n == 1:
        print(9)
    elif n == 2:
        print(98)
    else:
        s = '989'
        n -= 3
        s += st * (n // 10)
        s += st[:n % 10]
        print(s)
