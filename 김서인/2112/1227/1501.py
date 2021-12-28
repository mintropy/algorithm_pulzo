import sys
from collections import defaultdict

input = sys.stdin.readline
MIISS = lambda: map(int, input().strip().split())

N = int(input())
dictionary = [[defaultdict(int) for _ in range(53)] for _ in range(53)]
# 세로: 시작, 가로: 끝나는 글자. 대->소


def find_num(letter):
    letter_num = ord(letter)
    if 65 <= letter_num <= 90:  # 대문자이면
        return letter_num - 65
    else:
        return letter_num - 71


for _ in range(N):
    tmp = input().strip()  # 단어가 들어온다.

    # 그 단어가 한 글자인 경우..!
    if len(tmp) == 1:
        # 시작 글자
        start_num_final = find_num(tmp[0])

        dictionary[start_num_final][52][''.join(sorted(tmp[1:-1]))] += 1
        # 끝나는 글자 52 위치에 따로 처리..

    else:
        start, end = tmp[0], tmp[-1]

        # 시작 글자, 끝 글자 숫자 구하기
        start_num_final, end_num_final = find_num(start), find_num(end)

        dictionary[start_num_final][end_num_final][''.join(sorted(tmp[1:-1]))] += 1
        # 첫글자, 끝글자에 해당하는 리스트 위치에 딕셔너리 있음. key: 중간 글자들을 정렬해서 | value: 갯수 1 더함(디폴트 0)

M = int(input())
for _ in range(M):
    sentence = list(input().strip().split())  # 문장이 들어온다(한 단어 이상)

    ans = 1

    # 한 문장이 여러 단어로 이뤄져 있을 수 있음!!
    for i in range(len(sentence)):
        tmp = sentence[i]

        # 그 단어가 한 글자인 경우..!
        if len(tmp) == 1:
            start_num_final = find_num(tmp[0])

            ans *= dictionary[start_num_final][52][''.join(sorted(tmp[1:-1]))]

        else:
            start, end = tmp[0], tmp[-1]

            # 시작 글자, 끝 글자 숫자 구하기
            start_num_final, end_num_final = find_num(start), find_num(end)

            ans *= dictionary[start_num_final][end_num_final][''.join(sorted(tmp[1:-1]))]

    print(ans)
