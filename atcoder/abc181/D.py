# NTFS: spakk9(https://codeforces.com/blog/entry/84246?#comment-717655)
from collections import Counter


def main():
    s = input()
    ds = Counter(s)  # Counter of all chars
    if len(s) <= 2:
        if int(s) % 8 == 0 or int(
                s[::-1]) % 8 == 0:  # corner case because we can rearrange
            print("Yes")
        else:
            print("No")
        return
    for i in range(104, 1001, 8):  # Iterating over all 3 digit multiples of 8
        counter = Counter(str(i))  # comparing counters
        flag = 1
        for i in counter:
            if ds[i] < counter[i]:
                flag = 0
        if flag:
            print("Yes")
            return
    print("No")


main()