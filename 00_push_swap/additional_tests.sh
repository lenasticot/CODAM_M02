#!/bin/bash

echo "=== Test intensif 100 éléments ==="

SUCCESS=0
FAIL=0

for i in {1..100}; do
    ARG=$(shuf -i 1-5000 -n 100)
    RESULT=$(./push_swap $ARG | ./checker_linux $ARG)
    COUNT=$(./push_swap $ARG | wc -l)
    
    if [ "$RESULT" = "OK" ]; then
        SUCCESS=$((SUCCESS + 1))
        if [ $COUNT -le 700 ]; then
            echo "✓ Test $i: OK ($COUNT ops) - 5 points"
        elif [ $COUNT -le 900 ]; then
            echo "✓ Test $i: OK ($COUNT ops) - 4 points"
        elif [ $COUNT -le 1100 ]; then
            echo "✓ Test $i: OK ($COUNT ops) - 3 points"
        else
            echo "✓ Test $i: OK ($COUNT ops) - < 3 points"
        fi
    else
        FAIL=$((FAIL + 1))
        echo "✗ Test $i: $RESULT"
    fi
done

echo ""
echo "Résultats: $SUCCESS/100 réussis, $FAIL échecs"


