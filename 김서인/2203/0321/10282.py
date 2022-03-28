import sys, heapq

input = sys.stdin.readline

if __name__ == '__main__':
    INF = 10000 * 1000 + 1
    T = int(input())

    for _ in range(T):
        n, d, c = map(int, input().split())
        c -= 1  # 인덱스 편하게 쓰려고

        c_connect = [INF] * n
        board = list([] for _ in range(n))
        for _ in range(d):
            a, b, s = map(int, input().split())
            a -= 1
            b -= 1
            tmp = tuple((s, a))
            board[b].append(tmp)

        # 다익스트라
        visited = [False] * n
        q = []
        heapq.heappush(q, (0, c))
        while q:
            time, computer = heapq.heappop(q)  # 그 상황에 젤 가까운 컴퓨터
            if visited[computer]:  # 이미 방문했으면 넘어가기
                continue
            visited[computer] = True

            c_connect[computer] = time
            # 거기와 연결된 컴퓨터들 보기
            for i in range(len(board[computer])):
                time2, computer2 = board[computer][i]
                c_connect[computer2] = min(c_connect[computer2], c_connect[computer] + time2)
                heapq.heappush(q, (c_connect[computer2], computer2))

        # 정답 출력
        # cnt = 0
        # time = 0
        # for i in range(n):
        #     if c_connect[i] != INF:
        #         cnt += 1
        #         time = max(time, c_connect[i])

        # 정답 출력
        cnt = sum([1 for n in c_connect if n != INF])
        time = max([n for n in c_connect if n != INF])

        print(f'{cnt} {time}')
