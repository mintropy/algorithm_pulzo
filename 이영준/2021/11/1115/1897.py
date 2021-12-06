"""
Title : 토달기
Link : https://www.acmicpc.net/problem/1897
"""

import sys
input = sys.stdin.readline


d, string_0 = input().strip().split()
additional_strings = {}
for _ in range(int(d)):
    string = input().strip()
    if len(string) in additional_strings:
        additional_strings[len(string)].append(string)
    else:
        additional_strings[len(string)] = [string]
additional_strings[3] = [string_0]

max_word_len = 3
for i in range(4, 81):
    # 한 글자 추가해서 만들지 못할 때
    if i not in additional_strings:
        break
    possible_string = []
    # 길이가 i인 단어를 i - 1 길이로 만들 수 있는지
    for next_word in additional_strings[i]:
        for word in additional_strings[i - 1]:
            diff = 0
            idx0 = idx1 = 0
            while idx0 < i:
                if idx1 == i - 1:
                    diff +=1
                    break
                if next_word[idx0] == word[idx1]:
                    idx0 += 1
                    idx1 += 1
                else:
                    diff += 1
                    idx0 += 1
            if diff == 1:
                possible_string.append(next_word)
                break
    # 한 글자 추가해서 만들지 못할 때
    if not possible_string:
        break
    # 한 글자 추가해서 만들 수 있을 떄
    else:
        additional_strings[i] = possible_string[::]
        max_word_len = i

print(additional_strings[max_word_len][0])
