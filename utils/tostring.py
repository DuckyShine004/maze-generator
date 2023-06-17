from collections import defaultdict

from typing import List, Tuple

from time import sleep

class ToString:

	def __init__(self, rows: int, cols: int):
		self.__to_string_maze = defaultdict(list)

		self.__rows = rows
		self.__cols = cols

		self.initialize()

	def to_string(self):
		for _ in range(self.__cols):
			print(" _", end = "")

		print()

		for i in range(self.__rows):
			print("|", end = "")
			print(''.join(self.__to_string_maze[i]))

		print()

	def create_string(self, path: List[Tuple[int, int]], delay: bool = False):
		for i in range(len(path) - 1):
			if delay:
				self.to_string()
				sleep(0.1)

			u = path[i    ] 
			v = path[i + 1]

			r = v[0] - u[0]
			c = v[1] - u[1]

			if (r != 0):
				if (r > 0):
					self.set_string(u[0], u[1], "_")
				else:
					self.set_string(v[0], v[1], "_")

			if (c != 0):
				if (c > 0):
					self.set_string(u[0], u[1], "|")
				else:
					self.set_string(v[0], v[1], "|")

		if (not(delay)):
			self.to_string()

		print("Maze generated")	

	def initialize(self):
		for row in range(self.__rows):
			for col in range(self.__cols):
				self.__to_string_maze[row].append("_|")

	def set_string(self, row: int, col: int, string: str):
		self.__to_string_maze[row][col] = self.__to_string_maze[row][col].replace(string, " ")