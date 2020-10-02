from collections import defaultdict
n = int(input())
book = defaultdict(lambda : [])
for i in range(n):
    s = input().split()
    k = s[1]
    for j in s[2:]:
        book[s[0]].append(j)
final = defaultdict(lambda : [])
for entry in book:
    book[entry] = list(set(book[entry]))
    for i in book[entry]:
        flag = 0
        for j in book[entry]:
            if i == j:
                continue
            if j.endswith(i):
                flag = 1
        if not flag:
            final[entry].append(i)
print(len(final))
for entry in final:
    print(entry, len(final[entry]), ' '.join(final[entry]))