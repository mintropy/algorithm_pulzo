"""
title : ls
Link : https://www.acmicpc.net/problem/5015
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    pattern = input().strip()
    pattern_length = len(pattern)
    answer = ""
    for _ in range(int(input())):
        file_name = input().strip()
        file_name_length = len(file_name)
        file_name_idx = 0
        for pattern_idx, p in enumerate(pattern):
            if p == "*":
                if pattern_idx == pattern_length - 1:
                    continue
                if pattern[pattern_idx + 1] == "*":
                    continue
                next_pattern = pattern[pattern_idx + 1 :].split("*")[0]
                file_name_idx = file_name.find(next_pattern, file_name_idx)
                if file_name_idx == -1:
                    break
                continue
            if p != file_name[file_name_idx]:
                break
            file_name_idx += 1
        else:
            if pattern[-1] == "*" or pattern[-1] == file_name[-1]:
                answer += f"{file_name}\n"
    print(answer)
