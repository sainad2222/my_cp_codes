for _ in range(int(input())):
    n, c0, c1, h = map(int, input().split())
    s = input()
    n = len(s)
    zero = s.count('0')
    one = s.count("1")
    print(min(zero * c0+one * c1
    ,one*h+n * c0,zero*h+c1*n))