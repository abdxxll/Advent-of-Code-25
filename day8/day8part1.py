from itertools import combinations
from collections import Counter
import os

K = 1000  # number of closest pairs to connect


# ----- Disjoint Set Union (Union-Find) -----
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # path compression
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False  # already in same circuit
        # union by rank
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[rb] < self.rank[ra]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


def main():
    # ----- Read input -----
    points = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y, z = map(int, line.split(","))
            points.append((x, y, z))

    n = len(points)
    dsu = DSU(n)

    # ----- Build all pairwise distances -----
    pairs = []
    for i, j in combinations(range(n), 2):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        # squared distance is enough (no need for sqrt)
        d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        pairs.append((d2, i, j))

    # ----- Sort pairs by distance -----
    pairs.sort(key=lambda x: x[0])

    # ----- Connect the K closest pairs -----
    for idx in range(min(K, len(pairs))):
        _, a, b = pairs[idx]
        dsu.union(a, b)  # union is a no-op if already same circuit

    # ----- Count circuit sizes -----
    roots = [dsu.find(i) for i in range(n)]
    counts = Counter(roots)
    sizes = sorted(counts.values(), reverse=True)

    # Make sure there are at least 3 circuits
    while len(sizes) < 3:
        sizes.append(1)

    result = sizes[0] * sizes[1] * sizes[2]
    print("Sizes of three largest circuits:", sizes[:3])
    print("Answer:", result)


if __name__ == "__main__":
    main()
