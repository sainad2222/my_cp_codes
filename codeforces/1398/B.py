for _ in range(int(input())):
    s = input().replace('0','2').split('2')
    lis = []
    for i in s:
        lis.append(len(i))
    lis.sort(reverse=True)
    score = 0
    turn = True
    for i in lis:
        if turn:
            score += i
        turn = not turn
    print(score)