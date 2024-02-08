"""This module allows for the Kruskal maze generation algorithm to be 
efficient.
"""

from typing import List


class UnionFind:
    """The union find datastructure is particularly useful for finding
    and merging disjoin sets. It is preferred as it is performant and
    memory efficient.

    Attributes:
        rank (list): The height of each disjoint set.
        reps (list): List of disjoint sets.
    """

    def __init__(self, n: int):
        """Initializes the union find datastructure.

        Args:
            n (int): The number of initial disjoint sets.
        """

        self.reps: List[int] = list(range(n))
        self.rank: List[int] = [0] * n

    def find(self, x: int) -> int:
        """Finds and returns the parent/representative of element x.

        Args:
            x (int): The element of set X.

        Returns:
            int: Returns the parent/representative of element x.
        """

        while x != self.reps[x]:
            self.reps[x] = self.reps[self.reps[x]]
            x = self.reps[x]

        return x

    def union(self, x: int, y: int) -> bool:
        """Merges two disjoint sets - merges set X, and set Y, if possible.
        The merge is done based on the height of each disjoint tree.

        Args:
            x (int): The element of set X.
            y (int): The element of set Y.

        Returns:
            bool: Returns the result of the merge.
        """

        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        if self.rank[x] > self.rank[y]:
            self.reps[y] = x
        else:
            self.reps[x] = y

            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

        return True
