"""
Title : 명제 증명
Link : https://www.acmicpc.net/problem/2224
"""

from sys import stdin

input = stdin.readline


def ascii_to_index(x: int) -> int:
    if x < 97:
        return x - 65
    return x - (97 - 26)


def index_to_alp(x: int) -> str:
    if x < 26:
        return chr(x + 65)
    return chr(x + 97 - 26)


if __name__ == "__main__":
    N = int(input())
    propositions = [[False] * 52 for _ in range(52)]
    for _ in range(N):
        x, _, y = input().strip().split()
        x, y = ascii_to_index(ord(x)), ascii_to_index(ord(y))
        propositions[x][y] = True
    for k in range(52):
        for i in range(52):
            for j in range(52):
                if propositions[i][k] and propositions[k][j]:
                    propositions[i][j] = True
    ans = []
    for i in range(52):
        for j in range(52):
            if i != j and propositions[i][j]:
                x, y = index_to_alp(i), index_to_alp(j)
                ans.append(f"{x} => {y}")
    print(len(ans))
    print("\n".join(ans))
