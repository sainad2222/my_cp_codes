for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = ''
    for i in range(2*n):
        if i & 1 == 0:
            ans += s[i]
    print(ans)