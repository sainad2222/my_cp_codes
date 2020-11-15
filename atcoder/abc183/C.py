# import sys
# from collections import deque as queue
# sys.setrecursionlimit(10 ** 6)
# class Graph(object):

# 	def __init__(self):
# 		self.neighbours = {}
	
# 	def __repr__(self):
# 		s = ''
# 		for i in self.neighbours:
# 			s += str(i)+': '+' '.join(map(str,self.neighbours[i])) + '\n'
# 		return s
	
# 	def add_node(self, node):
# 		self.neighbours[node] = set()
	
# 	def add_edge(self, edge):
# 		u, v = edge
# 		self.neighbours[u].add(v)
# 		self.neighbours[v].add(u)
	
# 	def dfs(self, node):
# 		visited[node] = 1
# 		for child in self.neighbours[node]:
# 			if visited[child] == 0:
# 				self.dfs(child)
	

# n,k=map(int,input().split())
# matrix = []
# g = Graph()
# for i in range(n):
# 	g.add_node(i+1)
# for i in range(n):
# 	tmp = list(map(int,input().split()))
# 	matrix.append(tmp)

# for i in range(n):
# 	for j in range(i+1,n):
# 		g.add_edge((i+1,j+1))
# visited = [0] * (n + 1)
# print(g)
from itertools import permutations
n,k=map(int,input().split())
matrix = []
for i in range(n):
	tmp = list(map(int,input().split()))
	matrix.append(tmp)
path = [x for x in range(2,n+1)]
perm = list(permutations(path))
ans = 0
for per in perm:
	tmp = [1]+list(per)+[1]
	# print(tmp)
	cur_time = 0
	for i in range(1,n+1):
		cur_time += matrix[tmp[i]-1][tmp[i-1]-1]
	if cur_time==k:
		ans+=1
print(ans)