#!/bin/bash

echo "=== Edge cases ==="

# Un seul nombre
echo "Test: 1 nombre (42)"
./push_swap 42 | ./checker_linux 42
echo "Ops: $(./push_swap 42 | wc -l)"

# Deux nombres triés
echo "Test: 2 nombres triés (1 2)"
./push_swap 1 2 | ./checker_linux 1 2
echo "Ops: $(./push_swap 1 2 | wc -l)"

# Deux nombres non triés
echo "Test: 2 nombres non triés (2 1)"
./push_swap 2 1 | ./checker_linux 2 1
echo "Ops: $(./push_swap 2 1 | wc -l)"

# Grands nombres
echo "Test: grands nombres (2147483647 -2147483648 0)"
./push_swap 2147483647 -2147483648 0 | ./checker_linux 2147483647 -2147483648 0

# Duplicates (devrait afficher Error)
echo "Test: duplicates (1 2 2 3) - devrait être Error"
./push_swap 1 2 2 3

# Arguments invalides
echo "Test: non-int (1 abc 3) - devrait être Error"
./push_swap 1 abc 3

echo "Test: overflow (9999999999999) - devrait être Error"
./push_swap 9999999999999