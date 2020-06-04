for _ in range(int(input())):
    n = int(input())
    s = '{0:b}'.format(n)
    setBits = s.count('1')
    print(2*n-setBits)