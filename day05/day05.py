#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 05: Cafeteria

Determine which ingredient IDs are fresh based on range definitions.
An ingredient ID is fresh if it falls within any of the provided ranges.
"""
from typing import List, Tuple


def parse_input(data: str) -> Tuple[List[Tuple[int, int]], List[int]]:
    """
    Parse input into fresh ranges and available ingredient IDs.

    Args:
        data: Input data as string with ranges and IDs separated by blank line

    Returns:
        Tuple of (fresh_ranges, ingredient_ids) where:
        - fresh_ranges: List of (start, end) tuples for fresh ingredient ranges
        - ingredient_ids: List of available ingredient IDs to check
    """
    sections = data.strip().split('\n\n')

    # Parse fresh ranges (format: "start-end")
    range_lines = sections[0].strip().split('\n')
    fresh_ranges = []
    for line in range_lines:
        start, end = line.split('-')
        fresh_ranges.append((int(start), int(end)))

    # Parse available ingredient IDs
    id_lines = sections[1].strip().split('\n')
    ingredient_ids = [int(line) for line in id_lines]

    return fresh_ranges, ingredient_ids


def is_fresh(ingredient_id: int, ranges: List[Tuple[int, int]]) -> bool:
    """
    Check if an ingredient ID is fresh based on provided ranges.

    Args:
        ingredient_id: The ingredient ID to check
        ranges: List of (start, end) tuples representing fresh ingredient ranges

    Returns:
        True if ingredient ID falls within any range (inclusive), False otherwise
    """
    return any(start <= ingredient_id <= end for start, end in ranges)


def part1(data: str) -> int:
    """
    Count how many available ingredient IDs are fresh.

    Args:
        data: Input data as string

    Returns:
        Number of fresh ingredient IDs
    """
    fresh_ranges, ingredient_ids = parse_input(data)
    fresh_count = sum(1 for ingredient_id in ingredient_ids
                      if is_fresh(ingredient_id, fresh_ranges))
    return fresh_count


def merge_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Merge overlapping ranges into non-overlapping ranges.

    Args:
        ranges: List of (start, end) tuples

    Returns:
        List of merged (start, end) tuples with no overlaps
    """
    if not ranges:
        return []

    # Sort ranges by start position
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        # Check if current range overlaps or is adjacent to the last merged range
        if start <= last_end + 1:
            # Merge by extending the end of the last range
            merged[-1] = (last_start, max(last_end, end))
        else:
            # No overlap, add as new range
            merged.append((start, end))

    return merged


def part2(data: str) -> int:
    """
    Count total number of unique ingredient IDs covered by all ranges.

    Args:
        data: Input data as string

    Returns:
        Total count of unique ingredient IDs in all ranges
    """
    # Parse only the ranges section (ignore available IDs if present)
    sections = data.strip().split('\n\n')
    range_lines = sections[0].strip().split('\n')

    # Parse ranges
    ranges = []
    for line in range_lines:
        start, end = line.split('-')
        ranges.append((int(start), int(end)))

    # Merge overlapping ranges
    merged_ranges = merge_ranges(ranges)

    # Count total IDs in merged ranges
    total_count = sum(end - start + 1 for start, end in merged_ranges)

    return total_count


if __name__ == "__main__":
    with open('day05.dat', 'r', encoding='utf-8') as f:
        input_data = f.read().strip()

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
