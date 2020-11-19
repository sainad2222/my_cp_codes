for _ in range(int(input())):
    s = input()
    ans = 0
    one, two = 0, 0
    tmpone = s.count("(")
    tmptw0 = s.count("[")
    for char in s:
        if char == "(":
            one += 1
        elif char == ')':
            if one:
                one -= 1
        elif char == '[':
            two += 1
        else:
            if two:
                two -= 1
    print(tmpone-one+tmptw0-two)