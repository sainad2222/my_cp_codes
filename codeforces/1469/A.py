for _ in range(int(input())):
    s = input()
    n = len(s)
    if s[0] == ')' or s[-1] == '(' or n & 1:
        print("NO")
    else:
        print("YES")
