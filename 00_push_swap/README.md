*This project has been created as part of the 42 curriculum by leodum.*

# Push_swap

## Description

Push_swap is an algorithm project that sorts a stack of integers using a limited set of operations with the goal of minimizing the number of actions required.

**Project Goal:**
Sort data on stack A in ascending order using only two stacks (A and B) and a specific set of allowed operations.

**Key Concepts:**
- Sorting algorithms and their optimization
- Stack data structures (LIFO - Last In First Out)
- Algorithm complexity analysis
- Memory management in C

The program outputs a series of operations that, when executed, will sort the input stack. The challenge is to minimize the number of operations while maintaining code clarity and respecting the 42 Norm.

---

## Instructions

### Compilation
```bash
make
```

This will compile the project with the flags: `-Wall -Wextra -Werror`

### Usage
```bash
./push_swap [list of integers]
```

**Example:**
```bash
./push_swap 3 2 1 5 4
```

**Output:** A list of operations (sa, pb, ra, etc.)

### Using with Checker
```bash
ARG="4 67 3 87 23"; ./push_swap $ARG | ./checker $ARG
```

Expected output:
- `OK` if the stack is sorted
- `KO` if the stack is not sorted
- `Error` if there's an invalid operation or input

### Available Make Commands

- `make` - Compile the project
- `make clean` - Remove object files
- `make fclean` - Remove object files and executable
- `make re` - Recompile from scratch

---

## Resources

### Documentation & References

**Algorithm Theory:**
- [Radix Sort - GeeksforGeeks](https://www.geeksforgeeks.org/radix-sort/)
sorting-algorithms)
- [Stack Data Structure](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
- [Asymptotic Notations 101: Big O, Big Omega, & Theta (Asymptotic Analysis Bootcamp)] (https://www.youtube.com/watch?v=0oDAlMwTrLo&list=PLaRCVIXVlHUSu7ICY8iKSTJMHaCrKjwJm&index=6)

**Linked Lists in C:**
- [Doubly Linked List Implementation](https://www.geeksforgeeks.org/doubly-linked-list/)
- [Short introduction to doubly linked lists] (https://www.youtube.com/watch?v=9ArYyWQJgOU&list=PLfqABt5AS4FmXeWuuNDS3XGENJO1VYGxl&index=12)

### AI Usage

**Tasks where AI was used:**
- **Debugging assistance**: Helped identify logic errors in sorting functions and memory leaks
- **Algorithm explanation**: Clarified radix sort binary operations and bit manipulation
- **Edge case identification**: Helped identify test cases for error handling (overflow, duplicates, invalid input)

**Parts NOT done with AI:**
- Core algorithm implementation (radix sort, small number optimization)
- Data structure design (doubly linked list)
- All stack operations (push, swap, rotate, reverse rotate)
- Makefile structure
- Error handling logic

**AI was used as:**
- A rubber duck for explaining logic and catching mistakes
- A reference for C syntax and best practices
- A debugging companion, not a code generator

---

## Algorithm Overview

The program uses different strategies based on input size:

### Small Numbers (3-5 elements)
**Hardcoded optimal solutions**
- 3 elements: Maximum 3 operations
- 5 elements: Maximum 12 operations
- Strategy: Find smallest elements, push to B, sort remaining, push back

### Large Numbers (100-500 elements)
**Radix Sort Implementation**
- Sorts numbers by examining binary representation
- Processes one bit position at a time
- Average performance:
  - 100 elements: ~1000-1200 operations
  - 500 elements: ~6000-7500 operations

### Normalization
Before sorting, all numbers are converted to indices (0, 1, 2, ..., n-1) based on their relative size. This allows radix sort to work efficiently regardless of the actual input values.


## Evaluation Guidelines

### Basic Functionality Tests

**1. Simple Cases**
```bash
./push_swap 2 1                    # Should output: sa
./push_swap 1 2 3                  # Should output nothing (already sorted)
./push_swap 3 2 1 | wc -l          # Should be ≤ 3
```

**2. Error Cases**
```bash
./push_swap                        # No output (no arguments)
./push_swap 1 2 2                  # Should output: Error
./push_swap 1 abc 3                # Should output: Error
./push_swap 2147483648             # Should output: Error (overflow)
./push_swap "  "                   # Should output: Error
```

**3. With Checker**
```bash
./push_swap 5 4 3 2 1 | ./checker 5 4 3 2 1    # Should output: OK
```

### Performance Tests

**Count Operations:**
```bash
# 5 elements (should be ≤ 12)
ARG=$(shuf -i 1-100 -n 5); ./push_swap $ARG | wc -l

# 100 elements (check average over multiple runs)
for i in {1..5}; do
    ARG=$(shuf -i 1-5000 -n 100)
    echo "Test $i: $(./push_swap $ARG | wc -l) operations"
done
```

### Memory Leak Check
```bash
valgrind --leak-check=full ./push_swap 3 2 1
valgrind --leak-check=full ./push_swap 1 2 2 3  # Error case
```

## Project Structure
```
push_swap/
├── Makefile
├── README.md
├── push_swap.h
├── main.c
├── radixsort.c
├── smallsolving.c
├── create_list/
│   ├── create_llist.c
│   ├── parsing.c
│   └── error_check.c
└── operations/
    ├── push.c
    ├── swap.c
    ├── rotate.c
    └── reverse.c
```

---

## Performance Results

**Average results over 100 tests:**
- 3 elements: 2-3 operations
- 5 elements: 8-12 operations
- 100 elements: ~1084 operations (3-4 points)
- 500 elements: ~6784 operations (4-5 points)

---
