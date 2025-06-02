

class UnionFind:
    """
    A Union-Find (Disjoint-Set) data structure that supports efficient operations
    to find the root of a set and unite two sets. This implementation includes
    path compression and rank optimization to keep the tree structures shallow.

    Attributes:
        parent (List[int]): Parent list where parent[i] is the parent of element i.
                            If parent[i] == i, then i is the root of its set.
        rank (List[int]): Rank list to track the depth of the tree rooted at each element.
    """

    def __init__(self, n):
        """
        Initializes the Union-Find data structure with `n` elements.

        Each element is initially its own parent, representing `n` individual sets.
        The rank of all elements is initialized to 0.

        Args:
            n (int): The number of elements in the set, indexed from 0 to n-1.
        """
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """
        Finds the root of the set containing the element `x` with path compression.

        Path compression ensures that all elements on the path from `x` to the root
        point directly to the root, optimizing future operations.

        Args:
            x (int): The element whose set root is to be found.

        Returns:
            int: The root of the set containing `x`.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """
        Unites the sets containing elements `x` and `y` using rank optimization.

        The root of one set becomes the parent of the root of the other set based
        on the rank of the roots. This helps keep the tree structures shallow.

        Args:
            x (int): An element in the first set.
            y (int): An element in the second set.

        Returns:
            None
        """
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1