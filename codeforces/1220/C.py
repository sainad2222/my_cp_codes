s = input()
n = len(s)
print("Mike")
mi = s[0]
for i in range(1, n):
    if s[i] > mi:
        # if cur char greater than mi he can always choose l'
        print("Ann")
    else:
        # if cur char less than mi Ann cannot move anyway
        print("Mike")
    mi = min(mi, s[i])