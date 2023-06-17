from utils.tostring import ToString
from utils.maze import Maze

def main():
	rows = 10
	cols = 10

	maze = Maze(rows, cols)

	maze.generate()

	maze.to_string(delay = True)

if (__name__ == "__main__"):
	main()