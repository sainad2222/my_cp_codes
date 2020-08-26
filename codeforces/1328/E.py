from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip


def main():
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
    class Graph(object):

        def __init__(self):
            self.neighbours = {}
        
        def add_node(self, node):
            self.neighbours[node] = []
        
        def add_edge(self, edge):
            u, v = edge
            self.neighbours[u].append(v)
            self.neighbours[v].append(u)
        
        @bootstrap
        def dfs(self, v, parent, depth=0):
            parents[v] = parent
            depths[v] = depth
            visited[v] = 1
            intime[v] = timer[0]
            timer[0] += 1
            for child in self.neighbours[v]:
                if visited[child] == 0:
                    yield self.dfs(child, v, depth + 1)
            outtime[v] = timer[0]
            timer[0] += 1
            yield

    def inPath(x, y):
        return intime[x] <= intime[y] and outtime[x] >= outtime[y]

    g = Graph()
    n, q = map(int, input().split())
    for i in range(n):
        g.add_node(i + 1)
    for i in range(n - 1):
        x, y = map(int, input().split())
        g.add_edge((x, y))
    visited, intime, outtime = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    timer = [0]
    parents, depths = {}, {}
    g.dfs(1, -1)
    for i in range(q):
        lis = list(map(int, input().split()))[1:]
        deep = lis[0]
        for j in lis:
            if depths[deep] < depths[j]:
                deep = j
        for j in range(len(lis)):
            if lis[j] == deep:
                continue
            if parents[lis[j]]!=-1:
                lis[j] = parents[lis[j]]
        ok = True
        for j in lis:
            ok = ok & inPath(j, deep)
        print("YES") if ok else print("NO")






















# region fastio
# Credits
# # template credits to cheran-senthil's github Repo

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()