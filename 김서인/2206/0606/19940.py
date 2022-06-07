import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
directions = (-1, 1, -10, 10, 60)

for _ in range(T):
    N = int(input())
    initial_history1 = [0] * 5
    initial_history2 = [0] * 5

    # 시간 단위는 먼저 처리
    hour = N // 60
    initial_history1[-1] += hour
    initial_history2[-1] += (hour+1)

    target1 = N - (hour * 60)
    target2 = ((hour+1)*60) - N

    ans = 987654321

    def bfs(target, hour_type):
        visited = [False] * (target + 61)
        q = deque()
        if hour_type == 0:
            q.append([0, initial_history1[:]])
        else:
            q.append([0, initial_history2[:]])
        visited[0] = True

        while q:
            tmp_min, history = q.popleft()
            if tmp_min == target:
                return (sum(history), ' '.join(reversed(list(map(str, history)))))

            for k in range(5):
                kk = directions[k]
                next_min = tmp_min + kk
                if 0 <= next_min < target + 61 and not visited[next_min]:
                    new_history = history[:]
                    new_history[k] += 1
                    q.append([next_min, new_history])
                    visited[next_min] = True
    ans1, ans1_history = bfs(target1,0)
    ans2, ans2_history = bfs(target2,1)

    if ans1 > ans2:
        print(ans2_history)
    else:
        print(ans1_history)