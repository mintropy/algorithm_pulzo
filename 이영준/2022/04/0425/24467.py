"""
Title : 혼자 하는 윷놀이 
Link : https://www.acmicpc.net/problem/24467
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    pos = 0
    ans = "LOSE"
    next_pos = {5: 31, 10: 41, 33: 44}
    for _ in range(10):
        if pos == 50 and ans == "WIN":
            break
        yuts = input().strip()
        back_count = yuts.count("0")
        if back_count == 0:
            back_count = 5
        if pos in next_pos:
            pos = next_pos[pos]
            back_count -= 1
        pos += back_count
        if 35 < pos < 40:
            pos -= 19
        elif pos == 46 or pos == 20:
            pos = 50
        elif pos > 46 or 20< pos < 30:
            pos = 50
            ans = "WIN"
    print(ans)

'''
10  9  8  7  6  5
11  41      31  4
12    42  32    3
        33&43
13    34  44    2
14  35      45  1
15 16 17 18 19  0 / 50
'''
