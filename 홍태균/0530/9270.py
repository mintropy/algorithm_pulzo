'''
페그 솔리테어

'''
import sys
input = sys.stdin.readline
from copy import deepcopy
# N 값
N = int(input())

# 탐색
def dfs(pins,cnt):
    global maps, min_pin, min_cnt

    # 핀 개수가 죽어들면
    if len(pins) < min_pin:
        min_pin = len(pins)
        min_cnt = cnt
    # 핀 개수가 같을 때, 횟수가 줄어들면
    elif len(pins) == min_pin and cnt < min_cnt:
        min_pin = len(pins)
        min_cnt = cnt
    
    # 각 핀 마다 탐색
    for pin in pins:
        # 4방향 탐색
        for i in range(4):
            # 옆 확인
            next_x =  pin[0] + dirs[i][0]
            next_y =  pin[1] + dirs[i][1]
            # 뛰어 넘을 곳 확인
            ck_x = next_x + dirs[i][0]
            ck_y = next_y + dirs[i][1]
            # 옆이 핀이고 뛰어 넘을 수 있으면
            if maps[next_x][next_y] == 'o' and maps[ck_x][ck_y] == '.':
                # deepcopy로 복사
                next_pins = deepcopy(pins)
                # pins 사용을 갱신
                next_pins.remove(pin)
                next_pins.remove((next_x,next_y))
                next_pins.append((ck_x,ck_y))
                # 맵 핀 이동
                maps[pin[0]][pin[1]] = "."
                maps[next_x][next_y] = "."
                maps[ck_x][ck_y] = "o"
                dfs(next_pins, cnt+1)
                # 다시 초기화
                maps[pin[0]][pin[1]] = "o"
                maps[next_x][next_y] = "o"
                maps[ck_x][ck_y] = "."

# 각 맵 마다
for tc in range(N):
    # 맵에 패딩 주기
    maps = []
    maps.append(["#"] * 11)
    for _ in range(5):
        maps.append(["#"] + list(input().strip()) + ["#"])
    maps.append(["#"] * 11)
    if tc != N-1:
        input()    

    # 핀 위치 저장
    pins = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "o":
                pins.append((i,j))
    
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]

    min_pin = len(pins)
    min_cnt = 987654321
    
    dfs(pins,0)

    print(min_pin,min_cnt)