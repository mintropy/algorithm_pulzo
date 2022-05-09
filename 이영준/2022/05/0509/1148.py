"""
Title : 단어 만들기
Link : https://www.acmicpc.net/problem/1148
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    words = []
    while True:
        s = input().strip()
        if s == "-":
            break
        word = {}
        for t in s:
            if t not in word:
                word[t] = 1
            else:
                word[t] += 1
        words.append(word)
    while True:
        puzzle = input().strip()
        if puzzle == "#":
            break
        alphabets = {}
        for s in puzzle:
            if s in alphabets:
                alphabets[s][0] += 1
            else:
                alphabets[s] = [1, 0]
        for s in words:
            for k, v in s.items():
                if k not in alphabets or alphabets[k][0] < v:
                    break
            else:
                for k in s:
                    alphabets[k][1] += 1
        min_count, max_count = 200_000, 0
        min_ans, max_ans = [], []
        for k, v in alphabets.items():
            count = v[1]
            if count == min_count:
                min_ans.append(k)
            elif count < min_count:
                min_ans = [k]
                min_count = count
            if count == max_count:
                max_ans.append(k)
            elif count > max_count:
                max_ans = [k]
                max_count = count
        min_ans, max_ans = "".join(sorted(min_ans)), "".join(sorted(max_ans))
        print(f"{min_ans} {min_count} {max_ans} {max_count}")
