"""Pattern 11: union-find (disjoint set union) for dynamic connectivity."""


class UnionFind:
    """Union by rank plus path halving: near-constant amortised operations."""

    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        """Join the sets of a and b. False if they were already joined."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.components -= 1
        return True


def count_components(n: int, edges: list[list[int]]) -> int:
    uf = UnionFind(n)
    for a, b in edges:
        uf.union(a, b)
    return uf.components


def redundant_connection(edges: list[list[int]]) -> list[int] | None:
    """First edge (1-indexed nodes) that closes a cycle, or None."""
    if not edges:
        return None
    uf = UnionFind(max(max(edge) for edge in edges) + 1)
    for a, b in edges:
        if not uf.union(a, b):
            return [a, b]
    return None
