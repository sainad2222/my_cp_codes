for _ in range(int(input())):
	s = input()
	stack = []
	for char in s:
		if stack and char == "B" and (stack[-1] == "A" or stack[-1] == "B"):
			stack.pop()
		else:
			stack.append(char)
	print(len(stack))