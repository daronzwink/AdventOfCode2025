#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 07: Laboratories

Simulate tachyon beam splitting through a manifold. A beam enters at position S
moving downward. When a beam encounters a splitter (^), it stops and emits two
new beams from the left and right positions. Count total splits.
"""
from typing import List, Tuple
from collections import deque


def parse_grid(data: str) -> Tuple[List[str], Tuple[int, int]]:
    """
    Parse grid and find starting position.

    Args:
        data: Input data as string

    Returns:
        Tuple of (grid as list of strings, (start_row, start_col))
    """
    lines = data.strip().split('\n')

    # Find 'S' position
    for row_idx, line in enumerate(lines):
        col_idx = line.find('S')
        if col_idx != -1:
            return lines, (row_idx, col_idx)

    # Should never reach here with valid input
    raise ValueError("Starting position 'S' not found in grid")


def simulate_beam_splitting(grid: List[str], start_pos: Tuple[int, int]) -> int:
    """
    Simulate tachyon beam splitting through the manifold.

    Args:
        grid: List of strings representing the grid
        start_pos: Starting position (row, col) of initial beam

    Returns:
        Total number of unique splitters activated
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    queue = deque([start_pos])
    activated_splitters = set()
    visited = set([start_pos])  # Track visited positions to avoid reprocessing

    while queue:
        row, col = queue.popleft()

        # Move beam down one row
        new_row = row + 1

        # Check if beam exits grid
        if new_row >= rows:
            continue

        # Check column bounds
        if col < 0 or col >= cols:
            continue

        # Skip if we've already processed this position
        if (new_row, col) in visited:
            continue

        visited.add((new_row, col))

        # Get cell at new position
        cell = grid[new_row][col]

        if cell in ('.', 'S'):
            # Beam continues downward
            queue.append((new_row, col))
        elif cell == '^':
            # Record this splitter as activated
            activated_splitters.add((new_row, col))

            # Create two new beams at left and right positions
            # New beams start at same row as splitter
            left_col = col - 1
            right_col = col + 1

            # Enqueue left beam if in bounds
            if 0 <= left_col < cols:
                queue.append((new_row, left_col))

            # Enqueue right beam if in bounds
            if 0 <= right_col < cols:
                queue.append((new_row, right_col))

    return len(activated_splitters)


def count_timelines(grid: List[str], start_pos: Tuple[int, int]) -> int:
    """
    Count the number of distinct timelines in quantum mode.

    In quantum mode, a single particle takes both paths at each splitter,
    creating separate timelines via many-worlds interpretation. This function
    counts all possible paths from start to exit.

    Args:
        grid: List of strings representing the grid
        start_pos: Starting position (row, col) of initial particle

    Returns:
        Total number of distinct timelines
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    memo = {}

    def explore(row: int, col: int) -> int:
        """
        Count timelines from this position.

        Args:
            row: Current row
            col: Current column

        Returns:
            Number of timelines from this position
        """
        if (row, col) in memo:
            return memo[(row, col)]

        # Move down one row
        new_row = row + 1

        # Check if exited bottom
        if new_row >= rows:
            return 1

        # Check left/right bounds
        if col < 0 or col >= cols:
            return 1

        cell = grid[new_row][col]

        if cell in ('.', 'S'):
            # Continue downward in same timeline
            result = explore(new_row, col)
        elif cell == '^':
            # Quantum split: particle takes both paths
            # Count timelines from left + timelines from right
            left = explore(new_row, col - 1)
            right = explore(new_row, col + 1)
            result = left + right
        else:
            # Unknown cell, treat as exit
            result = 1

        memo[(row, col)] = result
        return result

    return explore(start_pos[0], start_pos[1])


def part1(data: str) -> int:
    """
    Count total beam splits in the tachyon manifold.

    Args:
        data: Input data as string

    Returns:
        Total number of beam splits
    """
    grid, start_pos = parse_grid(data)
    return simulate_beam_splitting(grid, start_pos)


def part2(data: str) -> int:
    """
    Count timelines in quantum tachyon manifold.

    Args:
        data: Input data as string

    Returns:
        Number of distinct timelines
    """
    grid, start_pos = parse_grid(data)
    return count_timelines(grid, start_pos)


if __name__ == "__main__":
    with open('day07.dat', 'r', encoding='utf-8') as f:
        input_data = f.read().strip()

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
