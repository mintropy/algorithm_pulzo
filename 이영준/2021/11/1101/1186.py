"""
Title : 직사각형 색칠하기
Link : https://www.acmicpc.net/problem/1186
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def compare_box(box: list) -> list:
    x1, y1, x2, y2 = MIIS()
    # 더 낮은 번호 가진 직사각형들 가려지는지 확인
    for i in range(len(box)):
        prev_box = []
        for x3, y3, x4, y4 in box[i]:
            # 완전 겹쳐질 때
            if x1 <= x3 and y1 <= y3 and x2 >= x4 and y2 >= y4:
                continue
            # 겹치지 않을 때
            elif x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3:
                prev_box.append((x3, y3, x4, y4))
            # 일부만 겹쳐질 때
            else:
                # 완전 내부
                if x1 > x3 and y1 > y3 and x2 < x4  and y2 < y4:
                    prev_box += [
                        (x3, y2, x1, y4), (x1, y2, x2, y4), (x2, y2, x4, y4), (x3, y1, x1, y2),
                        (x2, y1, x4, y2), (x3, y3, x1, y1), (x1, y3, x2, y1), (x2, y3, x4, y1)
                    ]
                # 2등분
                elif x1 <= x3 and y1 <= y3 and x3 < x2 < x4 and y2 >= y4:
                    prev_box.append((x2, y3, x4, y4))
                elif x3 < x1 < x4 and y1 <= y3 and x2 >= x4 and y2 >= y4:
                    prev_box.append((x3, y3, x1, y4))
                elif x1 <= x3 and y1 <= y3 and x2 >= x4 and y3 < y2 < y4:
                    prev_box.append((x3, y2, x4, y4))
                elif x1 <= x3 and y3 < y1 < y4 and x2 >= x4 and y2 >= y4:
                    prev_box.append((x3, y3, x4, y1))
                # 3등분 
                elif x3 < x1 < x4 and y1 <= y3 and x3 < x2 < x4 and y2 >= y4:
                    prev_box += [(x3, y3, x1, y4), (x2, y3, x4, y4)]
                elif x1 <= x3 and y3 < y1 < y4 and x2 >= x4 and y3 < y2 < y4:
                    prev_box += [(x3, y3, x4, y1), (x3, y2, x4, y4)]
                # 6등분
                elif x3 < x1 < x4 and y3 < y1 < y4 and x3 < x2 < x4 and y2 >= y4:
                    prev_box += [
                        (x3, y1, x1, y4), (x2, y1, x4, y4), (x3, y3, x1, y1), 
                        (x1, y3, x2, y1), (x2, y3, x4, y1)
                    ]
                elif x3 < x1 < x4 and y3 < y1 < y4 and x2 >= x4 and y3 < y2 < y4:
                    prev_box += [
                        (x3, y2, x1, y4), (x1, y2, x4, y4), (x3, y1, x1, y2), 
                        (x3, y3, x1, y1), (x1, y3, x4, y1)
                    ]
                elif x3 < x1 < x4 and y1 <= y3 and x3 < x2 < x4 and y3 < y2 < y4:
                    prev_box += [
                        (x3, y2, x1, y4), (x1, y2, x2, y4), (x2, y2, x4, y4), 
                        (x3, y3, x1, y2), (x2, y3, x4, y2)
                    ]
                elif x1 <= x3 and y3 < y1 < y4 and x3 < x2 < x4 and y3 < y2 < y4:
                    prev_box += [
                        (x3, y2, x2, y4), (x2, y2, x4, y4), (x2, y1, x4, y2), 
                        (x3, y3, x2, y1), (x2, y3, x4, y1)
                    ]
                # 4등분
                elif x1 <= x3 and y2 >= y4 and x3 < x2 < x4 and y3 < y1 < y4:
                    prev_box += [(x3, y3, x2, y1), (x2, y3, x4, y1), (x2, y1, x4, y4)]
                elif x2 >= x4 and y2 >= y4 and x3 < x1 < x4 and y3 < y1 < y4:
                    prev_box += [(x3, y3, x1, y1), (x1, y3, x4, y1), (x3, y1, x1, y4)]
                elif x1 <= x3 and y1 <= y3 and x3 < x2 < x4 and y3 < y2 < y4:
                    prev_box += [(x2, y3, x4, y2), (x3, y2, x2, y4), (x2, y2, x4, y4)]
                elif x2 >= x4 and y1 <= y3 and x3 < x1 < x4 and y3 < y2 < y4:
                    prev_box += [(x3, y3, x1, y2), (x3, y2, x1, y4), (x1, y2, x4, y4)]
        box[i] = prev_box
    # 지금 직사각형 추가
    box.append([(x1, y1, x2, y2)])
    return box


def calc_box_size(box_now: list) -> int:
    size = 0
    for x1, y1, x2, y2 in box_now:
        size += (x2 - x1) * (y2 - y1)
    return size


K, N = MIIS()
box = []
for _ in range(K):
    box = compare_box(box)

# 각 직사각형이 보이는 영역 넓이 구하기
box_size_viewd = []
for idx, box_now in enumerate(box):
    box_size_viewd.append((calc_box_size(box_now), idx))
# 정렬
box_size_viewd.sort(key=lambda x:(-x[0], x[1]))

ans = []
for _, idx in box_size_viewd[:N]:
    ans.append(idx + 1)
print(*sorted(ans))
