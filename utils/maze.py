from collections import defaultdict
from collections import deque

from random import randint

from typing import List, Tuple

from utils.tostring import ToString

class Maze:

	def __init__(self, rows: int, cols: int):
		self.__rows = rows
		self.__cols = cols

		self.__path = []

	def dfs(self, u: int, v: int, visited: List[Tuple[int, int]]):
		stack = deque()

		node = (u, v)

		stack.append(node)
		visited.add(node)

		while (stack):
			node = stack[-1]
			self.add_to_path(node)

			neighbors = self.get_neighbors(node, visited)

			if (neighbors):
				neighbor = neighbors[randint(0, len(neighbors) - 1)]

				stack.append(neighbor)
				visited.add(neighbor)
			else:
				stack.pop()

	def get_neighbors(self, node: Tuple[int, int], visited: List[Tuple[int, int]]):
		neighbors = []

		u, v = node

		point1 = (u + 1, v)
		point2 = (u - 1, v)
		point3 = (u, v + 1)
		point4 = (u, v - 1)

		if (self.check_neighbor(point1, visited)):
			neighbors.append(point1)

		if (self.check_neighbor(point2, visited)):
			neighbors.append(point2)

		if (self.check_neighbor(point3, visited)):
			neighbors.append(point3)

		if (self.check_neighbor(point4, visited)):
			neighbors.append(point4)

		return neighbors

	def check_neighbor(self, point: Tuple[int, int], visited: List[Tuple[int, int]]):
		u, v = point

		if (point not in visited):
			if (self.check_horizontal(v) and self.check_vertical(u)):
				return True

		return False

	def check_horizontal(self, v: int):
		return True if (v >= 0 and v < self.__cols) else False

	def check_vertical(self, u: int):
		return True if (u >= 0 and u < self.__rows) else False

	def add_to_path(self, node: Tuple[int, int]):
		self.__path.append(node)

	def clear_path(self):
		self.__path.clear()

	def get_path(self):
		return self.__path

	def generate(self):
		self.clear_path()

		u = 0
		v = 0

		visited = set()

		return self.dfs(u, v, visited)	

	def to_string(self, delay: bool = False):
		ToString(self.__rows, self.__cols).create_string(self.get_path(), delay)