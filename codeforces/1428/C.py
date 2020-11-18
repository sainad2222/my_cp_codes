for _ in range(int(input())):
    s = input()
    stack = 0
    prev = ''
    for char in s:
        if stack and char == 'B':
            stack -= 1
        else:
            stack += 1
            prev = char
    print(stack)