for _ in range(int(input())):
    n = int(input())
    k = (n // 4) + 1
    if n % 4 == 0:
        k -= 1
    print('9' * (n - k) + '8' * k)