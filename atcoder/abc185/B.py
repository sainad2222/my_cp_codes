n,m,t = map(int,input().split())
bank = n
prev = 0
flag = 1
for i in range(m):
    a,b = map(int,input().split())
    bank -= (a-prev)
    if bank<=0:
        flag = 0
    bank += (b-a)
    bank = min(n,bank)
    prev = b
bank -= (t - b)
if flag:
    if bank<=0:
        print("No")
    else:
        print("Yes")
else:
    print("No")
