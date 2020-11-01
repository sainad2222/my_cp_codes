def populate():
    lis = [0]
    for i in range(1, 10):
        lis.append(lis[-1] + i * (10**(i) - 10**(i - 1)))
    return lis


glob = populate()
n = input()
l = len(n)
print(glob[l - 1] + l * (1 + int(n) - (10**(l - 1))))