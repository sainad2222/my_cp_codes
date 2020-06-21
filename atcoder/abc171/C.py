n = int(input())
ans = ''
while n>0:
    n-=1
    r = n%26
    ans += chr(97+r)
    n=n//26
print(ans[::-1])