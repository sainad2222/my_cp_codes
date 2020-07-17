def check(a,b,c):
    if x==max(a,b) and y==max(a,c) and z==max(b,c):
        print("YES")
        print(a,b,c)
        return True
    return False
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    # a
    a = 1
    b = x
    c = y
    flag = 0
    if check(a,b,c):
        flag = 1
        continue
    # b
    a = x
    b = 1
    c = z
    if check(a,b,c):
        flag = 1
        continue
    # c
    a = y
    b = z
    c = 1
    if check(a,b,c):
        flag = 1
        continue
    if not flag:
        print("NO")