#!/bin/bash
g++ -shared -o game/pokemon_engine.so -fPIC game/pokemon_engine.cpp
echo "Compiled C++ engine to pokemon_engine.so"
