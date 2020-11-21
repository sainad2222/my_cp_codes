def check(i, j, char,char2):
    j+=1
    while j < n:
        if s[j] == char:
            return True
        j += 1
    i-=1
    while i >= 0:
        if s[i] == char2:
            return True
        i-=1
    return False
    
for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        print("YES") if check(x,y,s[y],s[x]) else print("NO")