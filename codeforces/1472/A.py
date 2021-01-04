for _ in range(int(input())):
    w, h, n = map(int, input().split())
    ans = 1
    while w & 1 == 0:
        ans *= 2
        w = w // 2
    while h & 1 == 0:
        ans *= 2
        h = h // 2
    print("YES") if n <= ans else print("NO")
