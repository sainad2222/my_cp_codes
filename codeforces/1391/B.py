for _ in range(int(input())):
    n, m = map(int, input().split())
    count = 0
    for i in range(n-1):
        tmp = input()
        if tmp[-1] == 'R':
            count += 1
    tmp = input()
    count += tmp.count("D")
    print(count)