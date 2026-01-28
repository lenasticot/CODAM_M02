#!/bin/bash

# Clone le visualizer (une seule fois)
if [ ! -d "push_swap_visualizer" ]; then
    git clone https://github.com/o-reo/push_swap_visualizer.git
    cd push_swap_visualizer
    mkdir build
    cd build
    cmake ..
    make
    cd ../..
fi

# Lance avec ton push_swap
ARG=$(shuf -i 1-100 -n 50)
./push_swap_visualizer/build/bin/visualizer $ARG