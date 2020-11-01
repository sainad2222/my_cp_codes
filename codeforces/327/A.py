n = int(input())
lis = list(map(int, input().split()))
s = ''.join(map(str, lis))
ans = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        count = s[:i].count("1")
        tmp = ""
        for char in s[i:j]:
            if char == '0':
                tmp += '1'
            else:
                tmp += '0'
        count += s[j:].count("1")
        ans = max(ans, count + tmp.count("1"))
print(ans)