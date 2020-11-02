n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append([x, y])


def check(a, b, c):
    return (c[1] - a[1]) * (b[0] - a[0]) == (b[1] - a[1]) * (c[0] - a[0])


def main():
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if check(points[i], points[j], points[k]):
                    print("Yes")
                    return
    print("No")


main()