for _ in range(int(input())):
    n = int(input())
    if n <= 30:
        print("NO")
    else:
        print("YES")
        if n == 36:
            print(6, 10, 15, 5)
        elif n == 40:
            print(6, 10, 15, 9)
        elif n == 44:
            print(6, 10, 15, 13)
        else:
            print(6, 10, 14, n - 30)