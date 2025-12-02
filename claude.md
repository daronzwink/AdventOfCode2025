# Claude Code - Advent of Code 2025 Workflow

This document provides a standardized workflow for completing each day's Advent of Code challenge with high quality and professionalism.

## Pre-Implementation Checklist

Before starting work on any day:
- [ ] Verify the day's directory exists (`dayXX/`)
- [ ] Read and understand the problem statement completely
- [ ] Note any example inputs and expected outputs

## Implementation Workflow

### 1. Setup Phase
- [ ] Ensure all required files exist:
  - `dayXX.py` - Main solution file
  - `dayXX.dat` - Puzzle input (initially empty, fill when provided)
  - `dayXX_example_part1.dat` - Example input for Part 1
  - `dayXX_example_part2.dat` - Example input for Part 2

### 2. Coding Standards
Follow these standards for all code:

**File Structure:**
```python
#!/usr/bin/env python3
"""
Advent of Code 2025 - Day XX: [Challenge Title]

[Brief description of the problem]
"""

def helper_functions():
    """Helper functions with clear docstrings"""
    pass

def part1(data):
    """
    Solution for Part 1.

    Args:
        data: Input data as string

    Returns:
        Solution for part 1
    """
    pass

def part2(data):
    """
    Solution for Part 2.

    Args:
        data: Input data as string

    Returns:
        Solution for part 2
    """
    pass

if __name__ == "__main__":
    with open('dayXX.dat', 'r', encoding='utf-8') as f:
        input_data = f.read().strip()

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
```

**Code Quality Requirements:**
- Clear, descriptive function names
- Comprehensive docstrings for all functions
- Type hints where appropriate
- Comments explaining complex logic (not obvious code)
- PEP 8 compliance
- Use `encoding='utf-8'` for all file operations

### 3. Part 1 Implementation
- [ ] Implement solution for Part 1
- [ ] Add puzzle input to `dayXX.dat`
- [ ] Add example input to `dayXX_example_part1.dat`
- [ ] Test with example input first
- [ ] Verify example produces expected output
- [ ] Run with actual puzzle input
- [ ] Document the answer

### 4. Part 2 Implementation
- [ ] Read Part 2 problem statement
- [ ] Add example input to `dayXX_example_part2.dat` (if different)
- [ ] Implement solution for Part 2
- [ ] Test with Part 2 example input
- [ ] Verify example produces expected output
- [ ] Run with actual puzzle input
- [ ] Document the answer

### 5. Quality Assurance

**CRITICAL: Run pylint and fix ALL issues**
```bash
cd dayXX
pipenv run pylint dayXX.py
```

- [ ] Code achieves 10.00/10 pylint score
- [ ] No warnings or errors
- [ ] If score is less than 10.00:
  - Review each issue
  - Fix or explicitly disable with justification
  - Re-run pylint until 10.00/10

**Additional Quality Checks:**
- [ ] Code is readable and well-documented
- [ ] No hardcoded values (except examples in comments)
- [ ] Functions are focused and single-purpose
- [ ] No unused imports or variables
- [ ] Consistent naming conventions

### 6. Documentation Updates

**Update README.md Progress:**
- [ ] Mark the completed day with `[x]` in the Progress section
- [ ] Verify the markdown renders correctly

Example:
```markdown
## Progress

- [x] Day 1
- [x] Day 2
- [x] Day 3  ← Update this line
```

### 7. Git Workflow

**Commit Message Template:**
```
Solve Day X: [Challenge Title] (Parts 1 & 2)

Implemented solution to [brief description]:
- Part 1: [what it does] (answer: [answer])
- Part 2: [what it does] (answer: [answer])

[Any notable implementation details or algorithms used]
Code passes pylint with 10.00/10 score.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Git Commands:**
- [ ] Stage files: `git add dayXX/ README.md`
- [ ] Check status: `git status`
- [ ] Review diff: `git diff --cached`
- [ ] Commit with proper message
- [ ] Push to GitHub: `git push`

## Post-Completion Checklist

After completing a day:
- [ ] Solution works correctly for both parts
- [ ] Pylint score is 10.00/10
- [ ] README.md progress is updated
- [ ] Changes are committed and pushed to GitHub
- [ ] Repository remains clean (no temporary files committed)

## Common Issues to Avoid

1. **Forgetting encoding parameter**
   - Always use `encoding='utf-8'` in `open()` calls

2. **Incomplete docstrings**
   - Every function needs a docstring with Args and Returns

3. **Not testing with examples first**
   - Always verify with example input before running actual input

4. **Skipping pylint**
   - NEVER skip the pylint check - it ensures code quality

5. **Forgetting to update README**
   - Update progress immediately after completing both parts

6. **Poor commit messages**
   - Follow the template for consistency and clarity

## File Organization

Each day should follow this structure:
```
dayXX/
├── dayXX.py                    # Main solution
├── dayXX.dat                   # Actual puzzle input
├── dayXX_example_part1.dat     # Example for Part 1
└── dayXX_example_part2.dat     # Example for Part 2
```

## Quick Reference Commands

```bash
# Navigate to day directory
cd dayXX

# Run solution
python3 dayXX.py

# Run pylint
pipenv run pylint dayXX.py

# Test with example input
python3 -c "
from dayXX import part1, part2
with open('dayXX_example_part1.dat', 'r', encoding='utf-8') as f:
    data = f.read().strip()
print(f'Part 1 Example: {part1(data)}')
print(f'Part 2 Example: {part2(data)}')
"

# Git workflow
git add dayXX/ README.md
git status
git diff --cached
git commit -m "Solve Day X: Title (Parts 1 & 2) ..."
git push
```

## Success Criteria

A day is considered complete when:
1. ✅ Both parts produce correct answers
2. ✅ Pylint score is 10.00/10
3. ✅ Code follows all quality standards
4. ✅ README.md is updated
5. ✅ Changes are committed and pushed
6. ✅ Repository is clean and professional

## Notes

- This workflow ensures consistency across all days
- Professional code quality makes the repository portfolio-ready
- Clear documentation helps future understanding
- Git history tells a clear story of progress

---

**Remember:** Quality over speed. Take time to write clean, well-documented code that you'd be proud to show to anyone.
