string = input().split("|")
s = [len(x) for x in string]
t = input()
if (s[0] + s[1] + len(t)) % 2:
    print("Impossible")
    exit()
mid = (s[0] + s[1] + len(t)) // 2
if not (s[0] <= mid and s[1] <= mid):
    print("Impossible")
    exit()
string[0] += t[:mid - s[0]]
string[1] += t[mid - s[0]:]
print(string[0] + "|" + string[1])
