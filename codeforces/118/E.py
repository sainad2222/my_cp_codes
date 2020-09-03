from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

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
    import time
    class Graph(object):

        def __init__(self):
            self.neighbours = {}
        
        def __repr__(self):
            s = ''
            for i in self.neighbours:
                s += str(i)+': '+' '.join(map(str,self.neighbours[i])) + '\n'
            return s
        
        def add_node(self, node):
            self.neighbours[node] = set()
        
        def add_edge(self, edge):
            u, v = edge
            self.neighbours[u].add(v)
            self.neighbours[v].add(u)

        @bootstrap
        def dfs(self, node, par):
            visited[node] = 1
            intime[node] = lowtime[node] = timer[0]
            timer[0] += 1
            for child in self.neighbours[node]:
                # if cur node's child is parent than for forward edge it is valid ancestor
                if child == par:
                    continue
                # even after checking for parent it is already visited than it is a back edge
                if visited[child] == 1:
                    if intime[node] > intime[child]:
                        lis.append([node,child])
                    # This is a back edge
                    # So we are updating the lowtime of cur node with intime of 
                    lowtime[node] = min(lowtime[node],intime[child])
                else:
                    # This is a forward edge
                    lis.append([node,child])
                    yield self.dfs(child, node)
                    # if low[child]<in[node]
                    # even if you remove this edge child is still connected from another path. so can't be a bridge
                    if lowtime[child] > intime[node]:
                        flag[0] = 0
                    lowtime[node] = min(lowtime[node],lowtime[child])
            yield
                

        
        def bfs(self, node):
            q = queue()
            visited[node] = 1
            q.append(node)
            while q:
                cur = q.popleft()
                for child in self.neighbours[cur]:
                    if visited[child] == 0:
                        q.append(child)
                        visited[child] = 1

    g = Graph()
    n,m=map(int,input().split())
    for i in range(n):
        g.add_node(i+1)
    for i in range(m):
        x, y = map(int, input().split())
        g.add_edge((x, y))
    visited = [0] * (n + 1)
    intime = [0] * (n + 1)
    lowtime = [0] * (n + 1)
    timer = [0]
    flag = [1]
    lis = []
    g.dfs(1, -1)
    if flag[0]:
        for i in lis:
            print(' '.join(map(str,i)))
    else:
        print(0)


if __name__ == "__main__":
    main()