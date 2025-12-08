#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 8: Playground

Connect junction boxes in 3D space using Union-Find algorithm.
Find the product of the three largest circuit sizes after making
the 1000 shortest connections.
"""


class DisjointSet:
    """
    Union-Find data structure for tracking circuits.

    Uses path compression and union by rank for optimal performance.
    """

    def __init__(self, n: int):
        """
        Initialize Disjoint Set with n elements.

        Args:
            n: Number of initial elements
        """
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x: int) -> int:
        """
        Find the root of x with path compression.

        Args:
            x: Element to find root for

        Returns:
            Root of the set containing x
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union two sets, returning whether a new connection was made.

        Args:
            x: First element
            y: Second element

        Returns:
            True if connection created, False if already connected
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already connected

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True


def parse_coordinates(data: str) -> list[tuple[int, int, int]]:
    """
    Parse input data into list of 3D coordinates.

    Args:
        data: Raw input data with coordinates

    Returns:
        List of (x, y, z) coordinates
    """
    return [tuple(map(int, line.split(','))) for line in data.splitlines()]


def euclidean_distance(p1: tuple[int, int, int],
                       p2: tuple[int, int, int]) -> float:
    """
    Calculate Euclidean distance between two 3D points.

    Args:
        p1: First point coordinates
        p2: Second point coordinates

    Returns:
        Euclidean distance between points
    """
    return ((p1[0] - p2[0])**2 +
            (p1[1] - p2[1])**2 +
            (p1[2] - p2[2])**2) ** 0.5


def part1(data: str) -> int:
    """
    Solution for Part 1.

    Connect the 1000 closest junction box pairs and find the product
    of the three largest circuit sizes.

    Args:
        data: Input data as string

    Returns:
        Product of three largest circuit sizes
    """
    coordinates = parse_coordinates(data)
    n = len(coordinates)

    # Compute all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            distances.append((dist, i, j))

    # Sort by distance
    distances.sort()

    # Attempt to connect 1000 closest pairs using DisjointSet
    disjoint_set = DisjointSet(n)
    attempts = 0

    for _, x, y in distances:
        disjoint_set.union(x, y)
        attempts += 1
        if attempts == 1000:
            break

    # Get circuit sizes (only count root nodes)
    circuit_sizes = [disjoint_set.size[i] for i in range(n)
                     if disjoint_set.find(i) == i]
    circuit_sizes.sort(reverse=True)

    # Return product of three largest
    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]


def part2(data: str) -> int:
    """
    Solution for Part 2.

    Connect pairs until all boxes form a single circuit.
    Return product of X coordinates of the last two boxes connected.

    Args:
        data: Input data as string

    Returns:
        Product of X coordinates of final connection
    """
    coordinates = parse_coordinates(data)
    n = len(coordinates)

    # Compute all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            distances.append((dist, i, j))

    # Sort by distance
    distances.sort()

    # Connect pairs until all in one circuit
    disjoint_set = DisjointSet(n)
    circuits = n  # Start with n separate circuits

    for _, x, y in distances:
        if disjoint_set.union(x, y):
            circuits -= 1  # Merged two circuits into one
            if circuits == 1:
                # All boxes now in one circuit
                # Return product of X coordinates
                return coordinates[x][0] * coordinates[y][0]

    return -1  # Should never reach here


if __name__ == "__main__":
    with open('day08.dat', 'r', encoding='utf-8') as f:
        input_data = f.read().strip()

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
