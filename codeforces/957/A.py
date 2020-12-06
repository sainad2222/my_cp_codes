def main():
    n = int(input())
    s = input()
    prev = ''
    for char in s:
        if char!='?' and char==prev:
            print("No")
            return
        prev = char
    if 'C?C' in s or 'M?M' in s or 'Y?Y' in s or '??' in s or s[0]=='?' or s[-1]=='?':
        print("Yes")
        return
    else:
        print("No")
        return
main()
