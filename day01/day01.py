#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 01
"""

def part1(data):
    """Count how many times dial points at 0"""
    lines = data.strip().split('\n')
    position = 50
    count = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if direction == 'L':
            position = (position - distance) % 100
        else:  # 'R'
            position = (position + distance) % 100

        if position == 0:
            count += 1

    return count

def part2(data):
    """Count how many times dial points at 0 during any click"""
    lines = data.strip().split('\n')
    position = 50
    count = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        # Count how many times we pass through 0 during this rotation
        if direction == 'R':
            count += (position + distance) // 100
        else:  # 'L'
            if position == 0:
                count += distance // 100
            else:
                count += (distance - position + 100) // 100

        # Update position
        if direction == 'L':
            position = (position - distance) % 100
        else:  # 'R'
            position = (position + distance) % 100

    return count

if __name__ == "__main__":
    with open('day01.dat', 'r', encoding='utf-8') as f:
        input_data = f.read().strip()

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
