for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    rev = sorted(lis, reverse=True)
    con_du = True
    if len(set(lis)) == len(lis):
        con_du = False
    if lis == rev and not con_du:
        print("NO")
    else:
        print("YES")