#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 02: Gift Shop

Find invalid product IDs in given ranges where an invalid ID is a number
consisting of some sequence of digits repeated exactly twice.
Examples: 55 (5 twice), 6464 (64 twice), 123123 (123 twice)
"""


def is_invalid_id_part1(num):
    """
    Check if a number is an invalid ID (pattern repeated exactly twice).

    Args:
        num: Integer to check

    Returns:
        True if the number is made of a pattern repeated exactly twice
    """
    s = str(num)

    # Must have even length to be repeated twice
    if len(s) % 2 != 0:
        return False

    # Split in half and check if both halves are identical
    half = len(s) // 2
    return s[:half] == s[half:]


def is_invalid_id_part2(num):
    """
    Check if a number is an invalid ID (pattern repeated at least twice).

    Args:
        num: Integer to check

    Returns:
        True if the number is made of a pattern repeated at least twice
    """
    s = str(num)
    n = len(s)

    # Try all possible pattern lengths from 1 to n/2
    for pattern_len in range(1, n // 2 + 1):
        # Check if n is divisible by pattern_len (so pattern repeats evenly)
        if n % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = n // pattern_len
            # repetitions will automatically be >= 2 since pattern_len <= n/2
            if pattern * repetitions == s:
                return True
    return False


def part1(data):
    """
    Find sum of all invalid IDs in the given ranges.

    Args:
        data: String containing comma-separated ranges (e.g., "11-22,95-115")

    Returns:
        Sum of all invalid IDs found in the ranges
    """
    # Parse comma-separated ranges
    ranges = []
    for range_str in data.strip().split(','):
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))

    # Find all invalid IDs and sum them
    total = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id_part1(num):
                total += num

    return total


def part2(data):
    """
    Find sum of all invalid IDs (repeated at least twice) in the given ranges.

    Args:
        data: String containing comma-separated ranges (e.g., "11-22,95-115")

    Returns:
        Sum of all invalid IDs found in the ranges
    """
    # Parse comma-separated ranges
    ranges = []
    for range_str in data.strip().split(','):
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))

    # Find all invalid IDs and sum them
    total = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id_part2(num):
                total += num

    return total


if __name__ == "__main__":
    with open('day02.dat', 'r', encoding='utf-8') as f:
        input_data = f.read().strip()

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
