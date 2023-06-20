from collections import defaultdict

from typing import List, Tuple

class Graph:

    def __init__(self):
        self.__graph = defaultdict(list)

    def add_edge(self, node1: Tuple[int, int], node2: Tuple[int, int]) -> None:
        if node2 not in self.__graph[node1]:
            self.__graph[node1].append(node2)

        if node1 not in self.__graph[node2]:
            self.__graph[node2].append(node1)

    def get_graph(self, path: List[Tuple[int, int]]) -> defaultdict:
        return self.__graph

