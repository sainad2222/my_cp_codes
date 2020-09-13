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
dpTD = {}
@bootstrap
def knapsackTD(wt,C):
    n = len(wt)
    if C in dpTD:
        yield dpTD[C]
    if C==0:
        yield 0
    ma = -float('inf')
    for coin in wt:
        if coin<=C:
            tmp_max = yield knapsackTD(wt,C-coin)
            if tmp_max + 1 > ma:
                ma = tmp_max + 1
    dpTD[C] = ma
    yield dpTD[C]
n, a, b, c = map(int, input().split())
wt = [a, b, c]
print(knapsackTD(wt,n))