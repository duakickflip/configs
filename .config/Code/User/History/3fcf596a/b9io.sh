#!/bin/bash
clang $1 main.c -o main.out -lm
./main.out