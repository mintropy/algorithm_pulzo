import sys
from collections import deque
input = sys.stdin.readline
N, S, P = map(int, input().split())
connections = [list(map(int, input().split())) for _ in range(N - 1)]
link = [[] for _ in range(N + 1)]
# 해당 인덱스에 연결된 얼음 인덱스들을 넣는다.
for s, e in connections:
    link[s].append(e)
    link[e].append(s)
answer = 0
life = 2
queue = deque([[P, 0, -1]])
while queue:
    curr, cnt, prev = queue.popleft()
    # 종료 조건: 도착한 얼음이 지지 얼음이면 그때까지의 카운트를 답에 더하고
    # 라이프를 하나 깍는다. 그 라이프가 0이 되면 종료한다.
    if curr <= S:
        answer += cnt
        life -= 1
        if life <= 0: break
    else:
        # 해당 얼음에서 갈 수 있는 얼음 중 이전 것을 제외하고 다음 얼음을 큐에 넣는다.
        next = link[curr]
        for e in next:
            if e != prev:
                queue.append([e, cnt + 1, curr])
# 총 얼음에서 저장된 값과 펭귄이 올라가 있는 값 1을 뺀 값을 출력한다.
print(N - answer - 1)