#NTFS: neharika_shah
from __future__ import division, print_function
from collections import defaultdict
mod = 1073741824

import os
import sys
from io import BytesIO, IOBase

def main():
	a,b,c = map(int,input().split())

	def primeFactors(n):
		dic = defaultdict(int)
		factors = []
		while n % 2 == 0:
			dic[2] += 1
			n = n // 2
		
		i = 3
		while i * i <= n:
			while n % i == 0:
				dic[i] += 1
				n = n // i
			i += 2
		
		if n > 2:
			dic[n] += 1
		return dic


	def calc(n):
		res = 1
		dic = primeFactors(n)
		for val in dic.values():
			res = (res*(val+1))%mod
		return res
	# print(calc(8))
	ans = 0
	for i in range(1,a+1):
		for j in range(1,b+1):
			for k in range(1,c+1):
				# print(calc(i*j*k))
				ans = (ans+calc(i*j*k))%mod
	print(ans)





















if sys.version_info[0] < 3:
	from __builtin__ import xrange as range
	from future_builtins import ascii, filter, hex, map, oct, zip

"""
region fastio
Credits
template credits to cheran-senthil's github Repo
"""

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



if __name__ == "__main__":
	main()


