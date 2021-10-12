'''
Puyo Puyo

'''
import sys
input = sys.stdin.readline
from copy import deepcopy

pan = [list(input().strip()) for _ in range(12)]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

# bfs
def bfs():
    global pan, chain
    ck = False

    # 전체 탐색
    for i in range(12):
        for j in range(6):
            # . 가 아닌 부분 찾기
            if pan[i][j] != '.':
                # 해당 색 저장
                pu_chr = pan[i][j]
                # 색깔이 나오면 카피 만들기(카피를 적게 하기위해서)
                copy_pan = deepcopy(pan)
            # 만약에 . 이 아니면 다음 인덱스 확인 
            else:
                continue

            # q 저장
            q = [(i,j)]
            # 해당 부분 . 으로 변경
            copy_pan[i][j] = '.'
            # 처음 부분이 1개이기 때문에 카운트는 1부터 시작
            cnt = 1
            # bfs 시작
            while q:
                node = q.pop(0)
                for dir in dirs:
                    ni = node[0] + dir[0]
                    nj = node[1] + dir[1]
                    # 범위 안에 있고 같은 색이면 q에 저장하고 . 로 바꾸고 카운드 증가
                    if 0 <= ni < 12 and 0<= nj < 6 and copy_pan[ni][nj] == pu_chr:
                        q.append((ni,nj))
                        copy_pan[ni][nj] = '.'
                        cnt += 1
            # 뿌요가 4개 이상이면 연쇄 발생
            if cnt >= 4:
                # 연쇄 발생을 확인하기위해
                ck = True
                # 연쇄가 발생했기 때문에 카피맵을 맵으로 저장
                pan = deepcopy(copy_pan)
    # 연쇄가 일어났으면 
    # 연쇄 증가에 1을 리턴
    if ck:
        chain += 1
        return 1
    # 연쇄가 안 일어나며 0 리턴
    else:
        return 0


# 연쇄 후 중력 작용
def down():
    global pan
    # 열 순으로 행을 확인
    for j in range(6):
        # 밑에서 부터 확인
        for i in range(11,-1,-1):
            # . 의 인덱스 확인
            if pan[i][j] == '.':
                dot_idx = i
            else:
                continue

            # . 위의 색 인덱스 확인 후 교환
            for k in range(i-1,-1,-1):
                if pan[k][j] != '.':
                    pan[k][j], pan[dot_idx][j] = pan[dot_idx][j],pan[k][j]
                    break
            # 만약에 위에 뿌요가 없다면 
            # 다음 열로 이동
            else:
                break
                
chain = 0
# 반복적으로 수행하기위해서 
# 연쇄가 발생하지 않을 때 까지 반복
while bfs():
    down()

print(chain)