n, x = map(int, input().split())
s = input()
for char in s:
    if char == 'o':
        x += 1
    else:
        if x > 0:
            x -= 1
            
print(x)