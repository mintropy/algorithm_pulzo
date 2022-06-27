"""
Title : LCS2
Link : https://www.acmicpc.net/problem/9252
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    string1, string2 = input().strip(), input().strip()
    lenght1, length2 = len(string1), len(string2)
    LCS = [[0] * (length2 + 1) for _ in range(lenght1 + 1)]
    for idx1, x in enumerate(string1):
        for idx2, y in enumerate(string2):
            if x == y:
                LCS[idx1][idx2] = LCS[idx1 - 1][idx2 - 1] + 1
            else:
                LCS[idx1][idx2] = max(LCS[idx1 - 1][idx2], LCS[idx1][idx2 - 1])
    max_count = LCS[lenght1 - 1][length2 - 1]
    x, y = lenght1 - 1, length2 - 1
    ans = []
    while LCS[x][y]:
        if LCS[x][y] == LCS[x - 1][y]:
            x -= 1
        elif LCS[x][y] == LCS[x][y - 1]:
            y -= 1
        else:
            ans.append(string1[x])
            x, y = x - 1, y - 1
    print(max_count)
    print("".join(ans[::-1]))
