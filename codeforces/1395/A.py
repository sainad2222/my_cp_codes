def check(r, g, b, w):
    count = 0
    if r & 1:
        count += 1
    if g & 1:
        count += 1
    if b & 1:
        count += 1
    if w & 1:
        count += 1
    if count > 1:
        return False
    return True
for _ in range(int(input())):
    r, g, b, w = map(int, input().split())
    if check(r, g, b, w):
        print("Yes")
        continue
    r, g, b, w = r - 1, g - 1, b - 1, w + 3
    if r < 0 or g < 0 or b < 0:
        print("No")
        continue
    if check(r, g, b, w):
        print("Yes")
        continue
    print("No")