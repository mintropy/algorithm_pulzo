"""
Title : 상자 배달
Link : https://www.acmicpc.net/problem/14947
"""

from collections import deque
import sys
input = sys.stdin.readline


def check(state: int, x: int, y: int) -> bool:
    global end
    if (x, y) == end:
        return True
    elif state == 1:
        if (x, y + 1) == end or (x, y - 1) == end:
            return True
    elif state == 2:
        if (x + 1, y) == end or (x - 1, y) == end:
            return True
    return False


def validate_grounds(state: int, x: int, y: int) -> bool:
    global grounds
    if (x, y) in grounds:
        return True
    elif state == 1:
        if (x, y - 1) in grounds and (x, y + 1) in grounds:
            return True
    elif state == 2:
        if (x - 1, y) in grounds and (x + 1, y) in grounds:
            return True
    return False


N, M = map(int, input().split())
delivery_map = [input().strip() for _ in range(N)]

grounds = set()
for i in range(N):
    for j in range(M):
        if delivery_map[i][j] == '1':
            grounds.add((i, j))
        elif delivery_map[i][j] == '2':
            grounds.add((i, j))
            st = (i, j)
        elif delivery_map[i][j] == '3':
            grounds.add((i, j))
            end = (i, j)

visited_vertical = [[False] * M for _ in range(N)]
visited_horizontal_garo = [[False] * M for _ in range(N)]
visited_horizontal_sero = [[False] * M for _ in range(N)]

visited_vertical[st[0]][st[1]] = True
# move count, state of box, position of box
queue = deque([(0, 0, st[0], st[1])])

ans = -2
while queue:
    count, state, x, y = queue.popleft()
    if check(state, x, y):
        ans = count
        break
    if state == 0:
        # left
        if y >= 3 and validate_grounds(1, x, y - 2):
            if not visited_horizontal_garo[x][y - 2]:
                visited_horizontal_garo[x][y - 2] = True
                queue.append((count + 1, 1, x, y - 2))
        # right
        if y <= M - 4 and validate_grounds(1, x, y + 2):
            if not visited_horizontal_garo[x][y + 2]:
                visited_horizontal_garo[x][y + 2] = True
                queue.append((count + 1, 1, x, y + 2))
        # up
        if x >= 3 and validate_grounds(2, x - 2, y):
            if not visited_horizontal_sero[x - 2][y]:
                visited_horizontal_sero[x - 2][y] = True
                queue.append((count + 1, 2, x - 2, y))
        # down
        if x <= N - 4 and validate_grounds(2, x + 2, y):
            if not visited_horizontal_sero[x + 2][y]:
                visited_horizontal_sero[x + 2][y] = True
                queue.append((count + 1, 2, x + 2, y))
    elif state == 1:
        # left
        if y >= 2 and validate_grounds(0, x, y - 2):
            if not visited_vertical[x][y - 2]:
                visited_vertical[x][y - 2] = True
                queue.append((count + 1, 0, x, y - 2))
        # right
        if y <= M - 3 and validate_grounds(0, x, y + 2):
            if not visited_vertical[x][y + 2]:
                visited_vertical[x][y + 2] = True
                queue.append((count + 1, 0, x, y + 2))
        # up
        if x >= 1 and validate_grounds(1, x - 1, y):
            if not visited_horizontal_garo[x - 1][y]:
                visited_horizontal_garo[x - 1][y] = True
                queue.append((count + 1, 1, x - 1, y))
        # down
        if x <= N - 2 and validate_grounds(1, x + 1, y):
            if not visited_horizontal_garo[x + 1][y]:
                visited_horizontal_garo[x + 1][y] = True
                queue.append((count + 1, 1, x + 1, y))
    else:
        # left
        if y >= 1 and validate_grounds(2, x, y - 1):
            if not visited_horizontal_sero[x][y - 1]:
                visited_horizontal_sero[x][y - 1] = True
                queue.append((count + 1, 2, x, y - 1))
        # right
        if y <= M - 2 and validate_grounds(2, x, y + 1):
            if not visited_horizontal_sero[x][y + 1]:
                visited_horizontal_sero[x][y + 1] = True
                queue.append((count + 1, 2, x, y + 1))
        # up
        if x >= 2 and validate_grounds(0, x - 2, y):
            if not visited_vertical[x - 2][y]:
                visited_vertical[x - 2][y] = True
                queue.append((count + 1, 0, x - 2, y))
        # down
        if x <= N - 3 and validate_grounds(0, x + 2, y):
            if not visited_vertical[x + 2][y]:
                visited_vertical[x + 2][y] = True
                queue.append((count + 1, 0, x + 2, y))

print(ans)


'''
# WA
# 다익스트라 방식으로 구현해보려 했는데 비효율적인거 같음
import heapq
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
delivery_map = [input().strip() for _ in range(N)]

grounds = set()
for i in range(N):
    for j in range(M):
        if delivery_map[i][j] == '1':
            grounds.add((i, j))
        elif delivery_map[i][j] == '2':
            st = (i, j)
        elif delivery_map[i][j] == '3':
            end = (i, j)

visited_vertical = [[1000] * M for _ in range(N)]
visited_horizontal_garo = [[1000] * M for _ in range(N)]
visited_horizontal_sero = [[1000] * M for _ in range(N)]

visited_vertical[st[0]][st[1]] = 0
# move_count, vertical or horizontal, position (if horizontal, center)
heap = [(0, 0, st)]

ans = -2
while heap:
    count, direction, (x, y) = heapq.heappop(heap)
    if end == (x, y)\
        or (direction == 1 and ((x, y + 1) == end or (x, y - 1) == end))\
        or (direction == 2 and ((x + 1, y) == end or (x - 1, y) == end)):
            ans = count
            break
    if direction == 0:
        # left
        if y >= 3 and ((x, y - 2) in grounds or ((x, y - 1) in grounds and (x, y - 3) in grounds)):
            if visited_horizontal_garo[x][y - 2] > count:
                visited_horizontal_garo[x][y - 2] = count + 1
                heapq.heappush(heap, (count + 1, 1, (x, y - 2)))
        # right
        if y <= M - 4 and ((x, y + 2) in grounds or ((x, y + 1) in grounds and (x, y + 3) in grounds)):
            if visited_horizontal_garo[x][y + 2] > count:
                visited_horizontal_garo[x][y + 2] = count + 1
                heapq.heappush(heap, (count + 1, 1, (x, y + 2)))
        # up
        if x >= 3 and ((x - 2, y) in grounds or ((x - 1, y) in grounds and (x - 3, y) in grounds)):
            if visited_horizontal_sero[x - 2][y] > count:
                visited_horizontal_sero[x - 2][y] = count + 1
                heapq.heappush(heap, (count + 1, 2, (x - 2, y)))
        # down
        if x <= N - 4 and ((x + 2, y) in grounds or ((x + 1, y) in grounds and (x + 3, y) in grounds)):
            if visited_horizontal_sero[x + 2][y] > count:
                visited_horizontal_sero[x + 2][y] = count + 1
                heapq.heappush(heap, (count + 1, 2, (x + 2, y)))
    elif direction == 1:
        # left
        if y >= 2 and (x, y - 2) in grounds:
            if visited_vertical[x][y - 2] > count:
                visited_vertical[x][y - 2] = count + 1
                heapq.heappush(heap, (count + 1, 0, (x, y - 2)))
        # right
        if y <= M - 3 and (x, y + 2) in grounds:
            if visited_vertical[x][y + 2] > count:
                visited_vertical[x][y + 2] = count + 1
                heapq.heappush(heap, (count + 1, 0, (x, y + 2)))
        # up
        if x >= 1 and ((x - 1, y) in grounds or ((x - 1, y - 1) in grounds and (x - 1, y + 1) in grounds)):
            if visited_horizontal_garo[x - 1][y] > count:
                visited_horizontal_garo[x - 1][y] = count + 1
                heapq.heappush(heap, (count + 1, 1, (x - 1, y)))
        # down
        if x <= N - 2 and ((x + 1, y) in grounds or ((x + 1, y - 1) in grounds and (x + 1, y + 1) in grounds)):
            if visited_horizontal_garo[x + 1][y] > count:
                visited_horizontal_garo[x + 1][y] = count + 1
                heapq.heappush(heap, (count + 1, 1, (x + 1, y)))
    else:
        # left
        if y >= 1 and ((x, y - 1) in grounds or ((x - 1, y - 1) in grounds and (x + 1, y - 1))):
            if visited_horizontal_sero[x][y - 1] > count:
                visited_horizontal_sero[x][y - 1] = count + 1
                heapq.heappush(heap, (count + 1, 2, (x, y - 1)))
        # right
        if y <= M - 2 and ((x, y + 1) in grounds or ((x - 1, y + 1) in grounds and (x + 1, y + 1))):
            if visited_horizontal_sero[x][y + 1] > count:
                visited_horizontal_sero[x][y + 1] = count + 1
                heapq.heappush(heap, (count + 1, 2, (x, y + 1)))
        # up
        if x >= 2 and (x - 2, y) in grounds:
            if visited_vertical[x - 2][y] > count:
                visited_vertical[x - 2][y] = count + 1
                heapq.heappush(heap, (count + 1, 0, (x - 2, y)))
        # down
        if x <= N - 3 and (x + 2, y) in grounds:
            if visited_vertical[x + 2][y] > count:
                visited_vertical[x + 2][y] = count + 1
                heapq.heappush(heap, (count + 1, 0, (x + 2, y)))

print(ans)
'''
