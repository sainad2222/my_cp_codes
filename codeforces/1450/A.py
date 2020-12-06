for _ in range(int(input())):
    n = int(input())
    s = input()
    cnt = s.count('t')
    if 't' in s:
        s = s.replace('t','')
    s += 't'*cnt
    print(s)
