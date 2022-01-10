"""
Title : Contact
Link : https://www.acmicpc.net/problem/1013
"""

import re
import sys
input = sys.stdin.readline


pattern = re.compile('(100+1+|01)+')

for _ in range(int(input())):
    s = input().strip()
    match = pattern.fullmatch(s)
    if match == None:
        print('NO')
    else:
        if match.end() == len(s):
            print('YES')
        else:
            print('NO')
