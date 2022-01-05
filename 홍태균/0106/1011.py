'''
Fly me to the Alpha Centauri

'''
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    x, y = map(int,input().split())
    # 거리
    ed = y - x
    # 이동거리
    step = 1
    # 거리가 몇인가
    idx = 0
    while 1:
        # 거리 1 증가
        idx += 1
        # 남은 거리 보다 적다면
        # 끝
        if ed - step <= 0:
            print(idx)
            break
        # 이동 거리만큼 줄이기
        ed -= step

        # 거리 1 증가
        idx += 1
        # 남은 거리 보다 적다면
        # 끝
        if ed - step <= 0:
            print(idx)
            break
        # 거리 줄이기
        ed -= step

        # 이동 거리 늘리기
        step += 1