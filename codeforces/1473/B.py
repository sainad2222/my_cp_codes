from math import gcd


def patt(inputv):
    if not inputv:
        return inputv

    nxt = [0] * len(inputv)
    for i in range(1, len(nxt)):
        k = nxt[i - 1]
        while True:
            if inputv[i] == inputv[k]:
                nxt[i] = k + 1
                break
            elif k == 0:
                nxt[i] = 0
                break
            else:
                k = nxt[k - 1]

    smallPieceLen = len(inputv) - nxt[-1]
    if len(inputv) % smallPieceLen != 0:
        return inputv

    return inputv[0:smallPieceLen]


for _ in range(int(input())):
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    if m > n:
        s, t = t, s
        n, m = m, n
    subs = patt(s)
    subt = patt(t)
    if subs != subt:
        print(-1)
        continue
    a, b = n // len(subs), m // len(subt)
    lcm = (a * b) // gcd(a, b)
    print(subs * (lcm))
