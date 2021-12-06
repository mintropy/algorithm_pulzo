'''
Title : 집합
Link : https://www.acmicpc.net/problem/11723
'''
# 비트 연산자 활용한 풀이

import sys

input = sys.stdin.readline

m = int(input())
bit_set = 0

def is_in(bit_set, num):
    if bit_set & 1<<num:
        return True
    return False

for _ in range(m):
    command = list(map(str, input().strip().split()))
    if command[0] == 'add':
        if not is_in(bit_set, int(command[1])):
            bit_set |= 1 << int(command[1])
    elif command[0] == 'remove':
        if is_in(bit_set, int(command[1])):
            bit_set -= 1 << int(command[1])
    elif command[0] == 'check':
        if is_in(bit_set, int(command[1])):
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if not is_in(bit_set, int(command[1])):
            bit_set |= 1 << int(command[1])
        else:
            bit_set -= 1 << int(command[1])
    elif command[0] == 'all':
        bin_max = '0b' + '1' * 20 + '0'
        bit_set = int(bin_max, 2)
    elif command[0] == 'empty':
        bit_set = 0
