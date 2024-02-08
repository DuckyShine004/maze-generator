class UnionFind:
    def __init__(self, n):
        self.reps = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        while x != self.reps[x]:
            self.reps[x] = self.reps[self.reps[x]]
            x = self.reps[x]

        return x

    def union(self, x, y):
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
