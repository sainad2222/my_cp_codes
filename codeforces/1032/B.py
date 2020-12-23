def ceil(a, b):
    return (a + b - 1) // b


s = input()
n = len(s)
if n <= 20:
    print(1, n)
    print(s)
else:
    rows = ceil(n, 20)
    cols = ceil(n, rows)
    stars = rows * cols - n
    eachRowStar, remStars = divmod(stars, rows)
    print(rows, cols)
    i = 0
    while i < n:
        if remStars > 0:
            print(s[i:i + cols - 1] + '*' * eachRowStar + '*')
            remStars -= 1
            i += (cols - 1)
        else:
            print(s[i:i + cols] + '*' * eachRowStar)
            i += cols
