"""
Title : S를 T로
Link : https://www.acmicpc.net/problem/3806
"""

from collections import defaultdict
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    for TC in range(int(input())):
        S = input().strip()
        T = input().strip()
        changes = defaultdict(int)
        for idx, s in enumerate(S):
            if s != T[idx]:
                changes[(s, T[idx])] += 1
        
        count = 0
        x = min(changes[('1', '0')], changes[('0', '1')])
        count += x
        changes[('1', '0')] -= x
        changes[('0', '1')] -= x
        
        x = min(changes[('1', '0')], changes[('?', '1')])
        count += x * 2
        changes[('1', '0')] -= x
        changes[('?', '1')] -= x
        
        if changes[('1', '0')]:
            count = -1
        else:
            count += changes[('0', '1')] + changes[('?', '0')] + changes[('?', '1')]
        print(f"Case {TC + 1}: {count}")

'''
(1, 0), (0, 1) 교환 : (1, 1), (0, 0)으로 1번으로 해결
(1, 0), (?, 1) 교환 : (1, 1), (?, 0)으로 변하므로 2번으로 해결
'''
