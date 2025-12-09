from itertools import combinations
import os

# ----- Disjoint Set Union (Union-Find) -----
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[rb] < self.rank[ra]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


def main():
    # ----- Read points -----
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
        d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2  # squared distance
        pairs.append((d2, i, j))

    # ----- Sort by distance -----
    pairs.sort(key=lambda x: x[0])

    # ----- Connect closest UNCONNECTED pairs until all in one circuit -----
    components = n
    last_pair = None

    for _, a, b in pairs:
        # Only connect if they are in different circuits
        if dsu.union(a, b):
            components -= 1
            last_pair = (a, b)
            if components == 1:
                break

    if last_pair is None:
        print("Something went wrong: never reached a single circuit.")
        return

    i, j = last_pair
    x1 = points[i][0]
    x2 = points[j][0]
    result = x1 * x2

    print("Last pair to connect:")
    print("  Box A:", points[i])
    print("  Box B:", points[j])
    print("X coordinates:", x1, x2)
    print("Answer (x1 * x2):", result)


if __name__ == "__main__":
    main()
