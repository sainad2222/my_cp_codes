n = int(input())
cnt={}
s = input()
for i in s:
    if i not in cnt:
        cnt[i]=1
    else:
        cnt[i]+=1
ans = ''
for a, b in cnt.items():
    if b % n:
        print(-1)
        exit(0)
    else:
        ans += a * (b // n)
print(ans * n)