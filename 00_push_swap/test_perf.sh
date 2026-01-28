#!/bin/bash

echo "=== Comptage d'opérations ==="

# 3 éléments (max 3 ops)
echo "3 éléments:"
for i in {1..10}; do
    ARG=$(shuf -i 1-100 -n 3)
    COUNT=$(./push_swap $ARG | wc -l)
    echo "  Test $i: $COUNT ops"
done

# 5 éléments (max 12 ops)
echo "5 éléments:"
for i in {1..10}; do
    ARG=$(shuf -i 1-100 -n 5)
    COUNT=$(./push_swap $ARG | wc -l)
    echo "  Test $i: $COUNT ops"
done

# 100 éléments
echo "100 éléments (10 tests):"
TOTAL=0
for i in {1..10}; do
    ARG=$(shuf -i 1-5000 -n 100)
    COUNT=$(./push_swap $ARG | wc -l)
    TOTAL=$((TOTAL + COUNT))
    echo "  Test $i: $COUNT ops"
done
AVG=$((TOTAL / 10))
echo "  Moyenne: $AVG ops"

# 500 éléments
echo "500 éléments (5 tests):"
TOTAL=0
for i in {1..5}; do
    ARG=$(shuf -i 1-5000 -n 500)
    COUNT=$(./push_swap $ARG | wc -l)
    TOTAL=$((TOTAL + COUNT))
    echo "  Test $i: $COUNT ops"
done
AVG=$((TOTAL / 5))
echo "  Moyenne: $AVG ops"