import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

import math

*N, _ = map(int, sys.stdin)
for v in N:
    print(math.factorial(v*2)//(math.factorial(v)*math.factorial(v+1)))