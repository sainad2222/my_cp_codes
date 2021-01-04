for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    lis = sorted(lis, reverse=True)
    alice, bob = 0, 0
    i = 0
    while i < n:
        if i & 1 == 0:
            if lis[i] & 1 == 0:
                alice += lis[i]
        else:
            if lis[i] & 1:
                bob += lis[i]
        i += 1
    if alice > bob:
        print("Alice")
    elif alice == bob:
        print("Tie")
    else:
        print("Bob")
