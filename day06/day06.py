#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 06: Trash Compactor

Parse and calculate results from a math worksheet where problems are arranged
in vertical columns. Each column contains numbers in the first 4 rows and an
operator (* or +) in the last row.
"""
from typing import List, Tuple


def find_column_boundaries(lines: List[str]) -> List[Tuple[int, int]]:
    """
    Find column boundaries by identifying contiguous regions with content.

    Args:
        lines: List of strings representing all rows of the worksheet

    Returns:
        List of (start, end) tuples representing column boundaries
    """
    # Find maximum line length
    max_len = max(len(line) for line in lines)

    # Create boolean array marking positions where ANY row has content
    has_content = [False] * max_len

    for line in lines:
        for i, char in enumerate(line):
            if char != ' ':
                has_content[i] = True

    # Find contiguous regions of True values
    columns = []
    in_column = False
    start = 0

    for i, has_char in enumerate(has_content):
        if has_char and not in_column:
            in_column = True
            start = i
        elif not has_char and in_column:
            in_column = False
            columns.append((start, i))

    # Handle last column if it extends to end
    if in_column:
        columns.append((start, len(has_content)))

    return columns


def calculate_column_result(lines: List[str], start: int, end: int) -> int:
    """
    Calculate the result for a single column.

    Args:
        lines: List of strings representing all rows
        start: Start index of column
        end: End index of column (exclusive)

    Returns:
        Result of the calculation for this column
    """
    # Get operator from last row
    operator = lines[-1][start:end].strip()

    # Get numbers from all rows except last
    numbers = []
    for row_idx in range(len(lines) - 1):
        text = lines[row_idx][start:end].strip()
        if text:
            numbers.append(int(text))

    # Calculate based on operator
    if operator == '+':
        return sum(numbers)
    if operator == '*':
        result = 1
        for num in numbers:
            result *= num
        return result
    return 0


def part1(data: str) -> int:
    """
    Calculate the grand total from the math worksheet.

    Args:
        data: Input data as string

    Returns:
        Grand total of all column calculations
    """
    lines = data.strip().split('\n')
    columns = find_column_boundaries(lines)

    grand_total = 0
    for start, end in columns:
        grand_total += calculate_column_result(lines, start, end)

    return grand_total


def calculate_column_result_cephalopod(lines: List[str], start: int, end: int) -> int:
    """
    Calculate the result for a single column using cephalopod math (right-to-left).

    In cephalopod math, each character column within a problem represents a separate
    number, read top-to-bottom (most to least significant digit), and we process
    columns right-to-left.

    Args:
        lines: List of strings representing all rows
        start: Start index of problem region
        end: End index of problem region (exclusive)

    Returns:
        Result of the calculation for this problem
    """
    # Get operator from last row
    operator = lines[-1][start:end].strip()

    # Collect numbers by reading each column position right-to-left
    numbers = []

    # Process each column position from right to left
    for col_pos in range(end - 1, start - 1, -1):
        # Extract digits from this column (all rows except operator row)
        digits = []
        for row_idx in range(len(lines) - 1):
            if col_pos < len(lines[row_idx]):
                char = lines[row_idx][col_pos]
                if char.isdigit():
                    digits.append(char)

        # Form number from digits (top to bottom = most to least significant)
        if digits:
            number = int(''.join(digits))
            numbers.append(number)

    # Calculate based on operator
    if operator == '+':
        return sum(numbers)
    if operator == '*':
        result = 1
        for num in numbers:
            result *= num
        return result
    return 0


def part2(data: str) -> int:
    """
    Calculate the grand total using cephalopod math (right-to-left reading).

    Args:
        data: Input data as string

    Returns:
        Grand total of all column calculations using cephalopod math
    """
    lines = data.strip().split('\n')
    columns = find_column_boundaries(lines)

    grand_total = 0
    for start, end in columns:
        grand_total += calculate_column_result_cephalopod(lines, start, end)

    return grand_total


if __name__ == "__main__":
    with open('day06.dat', 'r', encoding='utf-8') as f:
        input_data = f.read().strip()

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
