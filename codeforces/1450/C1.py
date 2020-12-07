# NTFS: secondthreadYT
for _ in range(int(input())):
    n = int(input())
    matrix = []
    
    # watch his video to get idea on why it works
    clrscnt = [0]*3
    colors = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        s = list(input())
        matrix.append(s)
        for j in range(n):
            colors[i][j]=(i+j)%3
            if s[j]=='X':
                clrscnt[(i+j)%3] += 1
    
    if clrscnt[0]==min(clrscnt):
        ans = 0
    elif clrscnt[1]==min(clrscnt):
        ans = 1
    else:
        ans = 2

    for i in range(n):
        for j in range(n):
            if matrix[i][j]=='X' and colors[i][j]==ans:
                matrix[i][j] = 'O'

    for row in matrix:
        print(''.join(row))
