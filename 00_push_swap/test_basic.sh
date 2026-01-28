#!/bin/bash

echo "=== Tests basiques ==="

# Cas simples
echo "Test: 2 1"
./push_swap 2 1 | ./checker_linux 2 1

echo "Test: 3 2 1"
./push_swap 3 2 1 | ./checker_linux 3 2 1

echo "Test: 1 3 2"
./push_swap 1 3 2 | ./checker_linux 1 3 2

# Déjà trié
echo "Test: déjà trié (1 2 3)"
./push_swap 1 2 3 | ./checker_linux 1 2 3

# Reverse trié
echo "Test: reverse (5 4 3 2 1)"
./push_swap 5 4 3 2 1 | ./checker_linux 5 4 3 2 1

# Nombres négatifs
echo "Test: nombres négatifs (-5 2 -1 0)"
./push_swap -5 2 -1 0 | ./checker_linux -5 2 -1 0