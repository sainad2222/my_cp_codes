x, y, a, b = map(int, input().split())
st = x
one = 0
two = 0
tmp = st
while tmp < b:
	if tmp * a >= y:
		break
	tmp *= a
	one += 1
two = (y - tmp) // b
if (y - tmp) % b == 0:
	two -= 1
print(one + two)