# NTFS: nwi
from collections import Counter, defaultdict
from string import ascii_letters, ascii_lowercase
s = input()
t = input()
yay, whoops = 0, 0
ds = Counter(s)
dt = Counter(t)

for char in ascii_letters:
    tmp = min(ds[char], dt[char])
    ds[char] -= tmp
    dt[char] -= tmp
    yay += tmp

for char in ascii_lowercase:
    ds[char] += ds[char.upper()]
    dt[char] += dt[char.upper()]
    tmp = min(ds[char], dt[char])
    ds[char] -= tmp
    dt[char] -= tmp
    whoops += tmp

print(yay, whoops)
