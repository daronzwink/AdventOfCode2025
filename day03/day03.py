#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 03: Lobby

Calculate maximum joltage from battery banks. Each bank requires selecting
exactly two batteries to form a two-digit joltage value. Find the maximum
possible joltage from each bank and sum them.
"""


def find_max_joltage(bank):
    """
    Find the maximum two-digit joltage from a battery bank.

    Strategy:
    - Try all pairs (i, j) where i < j
    - Calculate joltage as: digit[i] * 10 + digit[j]
    - Return the maximum value found

    Args:
        bank: String of digits representing battery joltage ratings

    Returns:
        Maximum two-digit joltage possible from the bank
    """
    max_joltage = 0
    for i, digit_i in enumerate(bank):
        for j in range(i + 1, len(bank)):
            joltage = int(digit_i) * 10 + int(bank[j])
            max_joltage = max(max_joltage, joltage)
    return max_joltage


def find_max_joltage_k_batteries(bank, k):
    """
    Find the maximum k-digit joltage from a battery bank.

    Uses a greedy algorithm to select k batteries that form the largest
    possible k-digit number while maintaining their original order.

    Strategy:
    - For each position in the result, choose the largest digit from the
      valid range (ensuring enough digits remain for subsequent positions)
    - Move past the chosen digit and repeat

    Args:
        bank: String of digits representing battery joltage ratings
        k: Number of batteries to select

    Returns:
        Maximum k-digit joltage possible from the bank
    """
    n = len(bank)
    if k > n:
        return 0

    result = []
    start = 0

    for i in range(k):
        # How many more digits do we need after this one?
        remaining_needed = k - i - 1
        # We must leave at least remaining_needed digits after our choice
        end = n - remaining_needed

        # Find the maximum digit in the valid range
        max_digit = max(bank[start:end])
        # Find its first occurrence in the valid range
        max_index = bank.index(max_digit, start, end)

        result.append(max_digit)
        start = max_index + 1

    return int(''.join(result))


def part1(data):
    """
    Calculate total output joltage from all battery banks.

    Args:
        data: Multi-line string, each line is a bank of batteries

    Returns:
        Sum of maximum joltages from all banks
    """
    lines = data.strip().split('\n')
    total = 0
    for line in lines:
        total += find_max_joltage(line)
    return total


def part2(data):
    """
    Calculate total output joltage using 12 batteries per bank.

    Args:
        data: Multi-line string, each line is a bank of batteries

    Returns:
        Sum of maximum 12-digit joltages from all banks
    """
    lines = data.strip().split('\n')
    total = 0
    for line in lines:
        total += find_max_joltage_k_batteries(line, 12)
    return total


if __name__ == "__main__":
    with open('day03.dat', 'r', encoding='utf-8') as f:
        input_data = f.read().strip()

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
