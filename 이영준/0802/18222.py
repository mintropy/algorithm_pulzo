"""
Title : 투에-모스 문자열
Link : https://www.acmicpc.net/problem/18222
"""


import sys, math
input = sys.stdin.readline

k = int(input())
first_4 = [0, 1, 1, 0]
tmp = [1, 0, 0, 1]

while True:
    if k <= 4:
        print(first_4[k - 1])
        break
    k_log_2 = int(math.log2(k))
    power_of_2 = 1 << k_log_2
    if k == power_of_2:
        power_of_2 //= 2
    k -= power_of_2
    first_4, tmp = tmp, first_4