for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    ones = sum([1 for x in lis if x == 1])
    twos = n - ones
    if twos & 1 == 0:
        print("YES") if ones & 1 == 0 else print("NO")
    else:
        print("YES") if ones & 1 == 0 and ones != 0 else print("NO")
