'''
총깡 총깡

문제
동물 애호가 진서는 총깡총깡 뛰는 동물과 짝폴짝폴 뛰는 동물들을 K마리씩 키운다. 타지로 취업하게 된 진서는 내일 이사를 한다.
이사하게 될 집에서 같이 살게 될 룸메이트 일호는 동물을 싫어하기 때문에 진서는 근처의 집에 동물들을 한마리씩 맡길 예정이다.
진서가 동물들을 맡길 수 있는 집의 종류는 A형 집과 B형 집 2종류 이다.
우연하게도 짝폴짝폴 뛰는 동물과 총깡총깡 뛰는 동물, A형 집, B형 집의 수는 모두 같다.

진서는 총깡총깡 뛰는 동물들과 짝폴짝폴 뛰는 동물들을 같은 종류의 집에 통일 시켜 맡기고 싶다.
하지만 진서는 총깡총깡 뛰는 동물들을 약간 더 좋아하므로 각 집에서 동시에 출발하여 진서네 집으로 
가장 빨리 도착하는 동물이 총깡총깡 뛰는 동물이길 원한다.
진서가 살게 될 집, A형 집, B형 집, A형 집도 B형 집도 아닌 집이 있는 지도가 주어질 때 총깡총깡 뛰는 동물이 
A형 집에 살아야 할 지 B형집에 살아야 할지 출력하고 가장 빨리 도착하는 총깡총깡 뛰는 동물이 진서네 집으로 부터 
얼마만큼 떨어져 있는지 출력하라.
(만약 총깡총깡 뛰는 동물들이 A형집에 살던 B형집에 살던 상관이 없는 경우는 A형집에 살기로 한다.)


입력
입력의 첫 번째 줄에 전체 집의 수 N과 집과 집사이를 연결하는 도로 M이 공백으로 주어진다. (3 ≤ N ≤ 5,000, 3 ≤ M ≤ 20,000)
입력의 둘째 줄에 진서의 집 J가 주어진다 (1 ≤ J ≤ N)
입력의 셋째 줄에 종류별 동물의 수 K가 주어진다. (2*K ≤ N)
입력의 넷째 줄에 K개의 A형 집이 공백으로 구분되어 주어진다.
입력의 다섯 번째 줄에 K개의 B형 집이 공백으로 구분되어 주어진다.
이후 M개의 줄에 X Y Z(1 ≤ X, Y ≤ N, 1 ≤ Z ≤ 100)가 주어진다. 
이는 X번 집과 Y번 집 사이에 Z의 길이를 가지는 도로가 존재한다는 것이다.


출력
총깡총깡 뛰는 동물이 살게 될 집의 종류를 말한 뒤 다음줄에 거리를 출력한다.
A형 집에서만 진서의 집에 갈 수 있는 경우 A를 출력한 뒤 다음 줄에 거리를 출력, 
B형 집에서만 진서의 집에 갈 수 있는 경우 B를 출력한 뒤 다음 줄에 거리를 출력, 
A형 집, B형 집 둘다 진서의 집에 갈 수 없는 경우에는 –1을 출력한다.
'''

import sys
import heapq
# 전체 집, 도로
N, M = map(int,sys.stdin.readline().split())
JS_Home = int(sys.stdin.readline())
# 동물 수
K = int(sys.stdin.readline())
A_homes = list(map(int,sys.stdin.readline().split())) 
B_homes = list(map(int,sys.stdin.readline().split()))

# 도로 저장
roads = [[] for _ in range(N+1)]
for _ in range(M):
    X, Y, Z = map(int,sys.stdin.readline().split())
    roads[X].append((Y,Z))
    roads[Y].append((X,Z))

# 거리 저장
INF = 100 * M + 1
distance = [INF] * (N+1)
distance[JS_Home] = 0

# 다익스트라
def dij(start):
    q = []
    heapq.heappush(q, [start,distance[start]])
    while q:
        cur_loc, cur_dis = heapq.heappop(q)
        if cur_dis > distance[cur_loc]:
            continue
        for next in roads[cur_loc]:
            next_loc, next_dis = next[0], next[1]
            if cur_dis + next_dis < distance[next_loc]:
                distance[next_loc] = cur_dis + next_dis
                heapq.heappush(q, [next_loc,cur_dis + next_dis])
dij(JS_Home)

# 거리가 0이기 때문에 다시 무한으로 만들기
distance[JS_Home] = INF

# A, B 둘다 아닌 집은 무한대로
for i in range(1,N+1):
    if i in A_homes or i in B_homes or i == JS_Home:
        continue
    else:
        distance[i] = INF

# 가장 적은 거리의 인덱스와 거리 구하기
min_idx = distance.index(min(distance))
min_dis = min(distance)

# 가장 적은 곳이 A인지 B인지
A_ck = False
B_ck = False
if min_idx in A_homes:
    A_ck = True
else:
    B_ck = True

# 짧은 거리의 집이 여러 개일 때 A,B 확인 
if distance.count(min_dis) > 1:
    for _ in range(distance.count(min_dis) - 1):
        min_idx = distance.index(min_dis,min_idx+1)
        if min_idx in A_homes:
            A_ck = True
        else:
            B_ck = True

# 확인
# 다 무한이면 갈 수 없음
if min_dis == INF:
    print(-1)
# A,B에 짧은 거리의 도로가 있을 경우 A 출력
elif A_ck and B_ck:
    print("A")
    print(min_dis)
# A 인 경우
elif min_idx in A_homes:
    print("A")
    print(min_dis)
# B 인 경우
else:
    print("B")
    print(min_dis)


'''
5 6
2
2
1 4
3 5
1 4 3
1 5 3
1 3 10
4 5 7
3 5 2
3 4 2


5 6
2
2
1 4
3 5
1 2 3
1 5 3
1 3 10
2 4 2
2 5 2
3 4 2

5 4
2
1
3
1
2 1 10
2 3 10
2 4 3
2 5 3
'''