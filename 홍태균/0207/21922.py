'''
학부 연구생 민상

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

# 맵을 저장하면서 
# 에어컨의 위치를 저장
maps = []
list_9 = []
for i in range(N):
    input_list = list(map(int,input().split()))
    for j in range(len(input_list)):
        if input_list[j] == 9:           
            x, y = i, j
            list_9.append((x,y))
    maps.append(input_list)

# 방문한 곳을 저장(결과 출력용) 
visit = [[0] * M for _ in range(N)]
# 방향
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

# dfs 하기 위한 q
q = []
# 일단 에어컨의 4방향을 담는다.
for x, y in list_9:
    visit[x][y] = 1
    q.extend([(x,y,0),(x,y,1),(x,y,2),(x,y,3)])
# 탐색
while q:
    now_x, now_y, now_dir = q.pop()
    # 다음 위치
    next_x, next_y = now_x + dirs[now_dir][0], now_y + dirs[now_dir][1]
    # 범위 안인지 확인
    if 0 <= next_x < N and 0 <= next_y < M:
        # 각 칸을 확인 
        # 0이면 같은 방향으로 지나가기
        if maps[next_x][next_y] == 0:
            q.append((next_x,next_y,now_dir))
        # 1이면 오른쪽(1), 왼쪽(3)만 막히고 다른 방향은 일정
        elif maps[next_x][next_y] == 1:
            if now_dir == 1 or now_dir == 3:
                pass
            else:
                next_dir = now_dir
                q.append((next_x,next_y,next_dir))
        # 2이면 위쪽(0), 아래쪽(2)만 막히고 다른 방향은 일정
        elif maps[next_x][next_y] == 2:
            if now_dir == 0 or now_dir == 2:
                pass
            else:
                next_dir = now_dir
                q.append((next_x,next_y,next_dir))
        # 3이면 위(0)는 오른쪽(1)으로 오른쪽은 위로/ 왼쪽(3)은 아래(2)로 아래는 왼쪽으로 방향이 바뀐다.
        elif maps[next_x][next_y] == 3:
            if now_dir == 0 or now_dir == 1:
                next_dir = 1 - now_dir
            else:
                next_dir = 5 - now_dir
            q.append((next_x,next_y,next_dir))
        # 4이면 위(0)는 왼쪽(3)으로 왼쪽은 위로/ 아래쪽(2)은 오른쪽(1)으로 오른쪽은 아래쪽으로 방향이 바뀐다.
        elif maps[next_x][next_y] == 4:
            next_dir = 3 - now_dir
            q.append((next_x,next_y,next_dir))
        visit[next_x][next_y] = 1

# 총 방문한 곳을 계산
result = 0
for vi in visit:
    result += sum(vi)
print(result)


# import sys
# input = sys.stdin.readline

# N, M = map(int,input().split())

# maps = []
# list_9 = []
# for i in range(N):
#     input_list = list(map(int,input().split()))
#     for j in range(len(input_list)):
#         if input_list[j] == 9:           
#             x, y = i, j
#             list_9.append((x,y))
#     maps.append(input_list)
    
# visit = [[[0] * M for _ in range(N)] for _ in range(2)]
# visit_count = [[0] * M for _ in range(N)]
         
# dirs = [(-1,0),(0,1),(1,0),(0,-1)]
# q = []
# for x, y in list_9:
#     visit[0][x][y] = 1
#     visit[1][x][y] = 1
#     visit_count[x][y] = 1
#     q.extend([(x,y,0),(x,y,1),(x,y,2),(x,y,3)])

# while q:
#     now_x, now_y, now_dir = q.pop()
    
#     next_x, next_y = now_x + dirs[now_dir][0], now_y + dirs[now_dir][1]
#     if 0 <= next_x < N and 0 <= next_y < M:
#         if maps[next_x][next_y] == 0:
#             if now_dir in [0,2] and visit[1][next_x][next_y] == 0:
#                 q.append((next_x,next_y,now_dir))
#                 visit[1][next_x][next_y] == 1
#             elif now_dir in [1,3] and visit[0][next_x][next_y] == 0:
#                 q.append((next_x,next_y,now_dir))
#                 visit[0][next_x][next_y] == 1
#         elif maps[next_x][next_y] == 1:
#             if now_dir == 1 or now_dir == 3:
#                 pass
#             else:
#                 next_dir = now_dir
#                 q.append((next_x,next_y,next_dir))
#         elif maps[next_x][next_y] == 2:
#             if now_dir == 0 or now_dir == 2:
#                 pass
#             else:
#                 next_dir = now_dir
#                 q.append((next_x,next_y,next_dir))
#         elif maps[next_x][next_y] == 3:
#             if now_dir == 0 or now_dir == 1:
#                 next_dir = 1 - now_dir
#             else:
#                 next_dir = 5 - now_dir
#             q.append((next_x,next_y,next_dir))
#         elif maps[next_x][next_y] == 4:
#             next_dir = 3 - now_dir
#             q.append((next_x,next_y,next_dir))
#         visit_count[next_x][next_y] = 1

# result = 0
# for vi in visit_count:
#     result += sum(vi)
# print(result)

# for i in visit_count:
#     print(*i)

'''
5 5
3 0 0 0 4
0 2 9 0 0
0 1 9 1 0
0 0 2 9 0
4 0 0 0 3

3 3
9 9 9
9 9 9
9 9 9
'''