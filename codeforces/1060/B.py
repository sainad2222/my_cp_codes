#NTFS: titia
s = input()
if len(s) == 1:
    print(s)
else:
    first = '9' * (len(s) - 1)
    second = int(s) - int(first)
    ans = 0
    for i in str(first) + str(second):
        ans += int(i)
    print(ans)
