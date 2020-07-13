for _ in range(int(input())):
    s = input()
    lenn = len(s)
    ma = max(s.count('P'),s.count('R'),s.count('S'))
    if s.count('P')==ma:
        print("S"*lenn)
    elif s.count('R')==ma:
        print("P"*lenn)
    else:
        print('R'*lenn)