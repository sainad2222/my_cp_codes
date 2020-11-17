def one(arr):
    x1, y1, x2, y2, x3, y3, x4, y4 = arr
    res = []
    if matrix[x1][y1] == '1':
        matrix[x1][y1] = '0'
        matrix[x2][y2] = '1'
        matrix[x3][y3] = '1'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x3 + 1)
        res.append(y3 + 1)
    elif matrix[x2][y2] == '1':
        matrix[x2][y2] = '0'
        matrix[x1][y1] = '1'
        matrix[x4][y4] = '1'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x4 + 1)
        res.append(y4 + 1)
    elif matrix[x3][y3] == '1':
        matrix[x1][y1] = '1'
        matrix[x2][y2] = '1'
        matrix[x3][y3] = '0'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x3 + 1)
        res.append(y3 + 1)
    elif matrix[x4][y4]=='1':
        matrix[x2][y2] = '1'
        matrix[x1][y1] = '1'
        matrix[x4][y4] = '0'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x4 + 1)
        res.append(y4 + 1)
    fin.append(res)
    two([x1, y1, x2, y2, x3, y3, x4, y4])
    return res


def two(arr):
    x1, y1, x2, y2, x3, y3, x4, y4 = arr
    res = []
    if matrix[x1][y1] == '1' and matrix[x4][y4] == '1':
        matrix[x1][y1] = '0'
        matrix[x2][y2] = '1'
        matrix[x3][y3] = '1'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x3 + 1)
        res.append(y3 + 1)
    elif matrix[x2][y2] == '1' and matrix[x3][y3] == '1':
        matrix[x2][y2] = '0'
        matrix[x1][y1] = '1'
        matrix[x4][y4] = '1'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x4 + 1)
        res.append(y4 + 1)
        # print(x1, y1, x2, y2, x3, y3, x4, y4)
    elif matrix[x1][y1] == '1' and matrix[x2][y2] == '1':
        matrix[x1][y1] = '0'
        matrix[x3][y3] = '1'
        matrix[x4][y4] = '1'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x3 + 1)
        res.append(y3 + 1)
        res.append(x4 + 1)
        res.append(y4 + 1)
    elif matrix[x3][y3] == '1' and matrix[x4][y4] == '1':
        matrix[x1][y1] = '1'
        matrix[x2][y2] = '1'
        matrix[x3][y3] = '0'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x3 + 1)
        res.append(y3 + 1)
    elif matrix[x2][y2] == '1' and matrix[x4][y4] == '1':
        matrix[x2][y2] = '0'
        matrix[x1][y1] = '1'
        matrix[x3][y3] = '1'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x3 + 1)
        res.append(y3 + 1)
    elif matrix[x1][y1] == '1' and matrix[x3][y3] == '1':
        matrix[x4][y4] = '1'
        matrix[x2][y2] = '1'
        matrix[x3][y3] = '0'
        res.append(x4 + 1)
        res.append(y4 + 1)
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x3 + 1)
        res.append(y3 + 1)
    fin.append(res)
    three([x1, y1, x2, y2, x3, y3, x4, y4])
    return res


def three(arr):
    x1, y1, x2, y2, x3, y3, x4, y4 = arr
    res = []
    if matrix[x1][y1] == '0':
        matrix[x2][y2] = '0'
        matrix[x3][y3] = '0'
        matrix[x4][y4] = '0'
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x3 + 1)
        res.append(y3 + 1)
        res.append(x4 + 1)
        res.append(y4 + 1)
    elif matrix[x2][y2] == '0':
        # print(x1, y1, x2, y2, x3, y3, x4, y4)
        matrix[x1][y1] = '0'
        matrix[x3][y3] = '0'
        matrix[x4][y4] = '0'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x3 + 1)
        res.append(y3 + 1)
        res.append(x4 + 1)
        res.append(y4 + 1)
    elif matrix[x3][y3] == '0':
        matrix[x2][y2] = '0'
        matrix[x1][y1] = '0'
        matrix[x4][y4] = '0'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x4 + 1)
        res.append(y4 + 1)
    elif matrix[x4][y4] == '0':
        matrix[x1][y1] = '0'
        matrix[x2][y2] = '0'
        matrix[x3][y3] = '0'
        res.append(x1 + 1)
        res.append(y1 + 1)
        res.append(x2 + 1)
        res.append(y2 + 1)
        res.append(x3 + 1)
        res.append(y3 + 1)
    fin.append(res)
    return res


def four(arr):
    res = []
    x1, y1, x2, y2, x3, y3, x4, y4 = arr
    matrix[x1][y1] = '0'
    matrix[x2][y2] = '0'
    matrix[x3][y3] = '0'
    res.append(x1 + 1)
    res.append(y1 + 1)
    res.append(x2 + 1)
    res.append(y2 + 1)
    res.append(x3 + 1)
    res.append(y3 + 1)
    fin.append(res)
    one([x1, y1, x2, y2, x3, y3, x4, y4])
    return res


for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        tmp = input()
        tmp = list(tmp)
        matrix.append(tmp)
    fin = []
    for i in range(n - 1):
        for j in range(m - 1):
            cnt = 0
            if matrix[i][j] == '1':
                cnt += 1
            if matrix[i][j + 1] == '1':
                cnt += 1
            if matrix[i + 1][j] == '1':
                cnt += 1
            if matrix[i + 1][j + 1] == '1':
                cnt += 1
            # print([i, j, i, j + 1, i + 1, j, i + 1, j + 1])
            if cnt == 0:
                continue
            if cnt == 1:
                one([i, j, i, j + 1, i + 1, j, i + 1, j + 1])
            elif cnt == 2:
                two([i, j, i, j + 1, i + 1, j, i + 1, j + 1])
            elif cnt == 3:
                three([i, j, i, j + 1, i + 1, j, i + 1, j + 1])
            else:
                four([i, j, i, j + 1, i + 1, j, i + 1, j + 1])
    # print(matrix)
    print(len(fin))
    for i in fin:
        print(*i)