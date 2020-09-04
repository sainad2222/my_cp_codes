for _ in range(int(input())):
    a, b, x, y, n = map(int, input().split())
    # ac, bc = 0, 0
    # if a < b:
    #     if n <= (a-x):
    #         ac = n
    #     else:
    #         ac = a - x
    #         n -= (a - x)
    #         bc = min((b - y), n)
    # else:
    #     if n <= (b-y):
    #         bc = n
    #     else:
    #         bc = b - y
    #         n -= (b - y)
    #         ac = min((a - x), n)
    # print((a - ac) * (b - bc))
    tmp = n
    ac, bc = 0, 0
    if n <= (a - x):
        ac = n
    else:
        ac = a - x
        n -= ac
        bc = min((b - y), n)
    cost1 = (a - ac) * (b - bc)
    
    n = tmp
    ac, bc = 0, 0
    if n <= (b - y):
        bc = n
    else:
        bc = b - y
        n -= bc
        ac = min((a - x), n)
    cost2 = (a - ac) * (b - bc)
    print(min(cost1, cost2))