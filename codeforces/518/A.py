s = input()
t = input()
s = [ord(i) - 96 for i in s]
t = [ord(i) - 96 for i in t]


def check(s, t):
    if s == t:
        return False
    for i, j in zip(s, t):
        if i < j:
            return True
        if i > j:
            return False
    return True


cur = len(s) - 1
flag = 1
while True:
    if s[cur] >= 26:
        s[cur] = 1
        cur -= 1
        if cur == -1:
            flag = 0
            break
        continue
    s[cur] += 1
    cur -= 1
    # print(s, t)
    if check(s, t):
        break
    if cur == -1:
        flag = 0
        break
s = [chr(i + 96) for i in s]
print(''.join(s)) if flag else print("No such string")