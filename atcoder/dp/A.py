from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
n = int(input())
lis = list(map(int, input().split()))
dp = {}
@bootstrap
def TD(i):
    if i == n - 1:
        yield 0

    if i in dp:
        yield dp[i]
    mi = float('inf')
    for j in range(1, 3):
        if i + j < n:
            tmp = yield TD(i+j)
            mi = min(mi, abs(lis[i] - lis[i+j])+ tmp)
    dp[i] = mi
    yield mi
print(TD(0))   