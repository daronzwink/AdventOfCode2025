#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 04: Printing Department

Determine which rolls of paper can be accessed by forklifts based on
the number of adjacent rolls.
"""

def count_adjacent_rolls(grid, row, col):
    """
    Count the number of rolls (@) adjacent to the given position.

    Args:
        grid: 2D list/grid of characters
        row: Row index
        col: Column index

    Returns:
        Number of '@' symbols in the 8 adjacent positions
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    # Define the 8 adjacent directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Top-left, top, top-right
        (0, -1),           (0, 1),   # Left, right
        (1, -1),  (1, 0),  (1, 1)    # Bottom-left, bottom, bottom-right
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        # Check if the position is within bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == '@':
                count += 1

    return count

def part1(data):
    """
    Count rolls of paper that can be accessed by forklifts.
    A roll can be accessed if it has fewer than 4 adjacent rolls.

    Args:
        data: Input data as string

    Returns:
        Number of accessible rolls
    """
    # Parse the grid
    grid = data.split('\n')

    accessible_count = 0

    # Iterate through each position in the grid
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            # Check if this position has a roll
            if cell == '@':
                # Count adjacent rolls
                adjacent = count_adjacent_rolls(grid, row_idx, col_idx)

                # A roll is accessible if it has fewer than 4 adjacent rolls
                if adjacent < 4:
                    accessible_count += 1

    return accessible_count

def part2(data):
    """
    Count total rolls that can be removed by iteratively removing accessible rolls.
    A roll is accessible if it has fewer than 4 adjacent rolls.
    Keep removing accessible rolls until no more can be removed.

    Args:
        data: Input data as string

    Returns:
        Total number of rolls that can be removed
    """
    # Parse the grid into a mutable list of lists
    grid = [list(row) for row in data.split('\n')]

    total_removed = 0

    while True:
        # Find all accessible rolls in this iteration
        accessible_positions = []

        for row_idx, row in enumerate(grid):
            for col_idx, cell in enumerate(row):
                if cell == '@':
                    adjacent = count_adjacent_rolls(grid, row_idx, col_idx)
                    if adjacent < 4:
                        accessible_positions.append((row_idx, col_idx))

        # If no rolls are accessible, we're done
        if not accessible_positions:
            break

        # Remove all accessible rolls
        for row_idx, col_idx in accessible_positions:
            grid[row_idx][col_idx] = '.'

        # Add to total count
        total_removed += len(accessible_positions)

    return total_removed

if __name__ == "__main__":
    with open('day04.dat', 'r', encoding='utf-8') as f:
        input_data = f.read().strip()

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
