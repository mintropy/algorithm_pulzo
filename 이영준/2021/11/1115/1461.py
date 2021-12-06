"""
Title : 도서관
Link : https://www.acmicpc.net/problem/1461
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


n, m = MIIS()
books = MIIS()

# 양수 좌표, 음수 좌표로 나누가
positives = []
negatives = []
for book in books:
    if book > 0:
        positives.append(book)
    else:
        negatives.append(abs(book))

positives.sort(reverse=True)
negatives.sort(reverse=True)

positive_times = positives[::m]
negative_times = negatives[::m]


# 조건별로 처리 >> 출력
if not positive_times:
    print(sum(negative_times) * 2 - negative_times[0])
elif not negative_times:
    print(sum(positive_times) * 2 - positive_times[0])
elif positive_times[0] >= negative_times[0]:
    print((sum(positive_times) + sum(negative_times)) * 2 - positive_times[0])
elif positive_times[0] < negative_times[0]:
    print((sum(positive_times) + sum(negative_times)) * 2 - negative_times[0])
