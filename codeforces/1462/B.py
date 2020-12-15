for _ in range(int(input())):
    n = int(input())
    s = input()
    if s[:4]=='2020' or s[n-4:]=='2020' or s=='2020':
        print("YES")
    elif s[n-3:n]=='020' and s[0]=='2':
        print("YES")
    elif s[n-2:n]=='20' and s[:2]=='20':
        print("YES")
    elif s[n-1]=='0' and s[:3]=='202':
        print("YES")
    else:
        print("NO")
