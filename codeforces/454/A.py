n = int(input())
row = 1
flag = False
for i in range(n):
    tmp = (n - row) // 2
    print("*" * tmp + "D" * row + "*" * tmp)
    if not flag:
        row += 2
    else:
        row -= 2
    if row > n:
        row -= 4
        flag = True
