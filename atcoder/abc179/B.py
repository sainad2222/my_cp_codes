n = int(input())
lis = ''
for i in range(n):
    a, b = map(int, input().split())
    if a == b:
        lis+='1'
    else:
        lis += '0'
if '111' in lis:
    print("Yes")
else:
    print("No")