from collections import deque
def sol():
    N, K = map(int, input().split())

    # 수빈이가 동생보다 큰 좌표에 있으면 걸어서 이동만 가능
    if K <= N:
        return N - K
    # 큐에는 수빈이의 현 좌표와 이동 시간
    queue = deque([[N, 0]])
    # 방문한 노드 표시를 위한 ㄷㅅㄴㄹ
    visited = {}
    while queue:
        location, cnt = queue.popleft()
        # 현위치가 동생위치면 끝
        if location == K:
            return cnt
        # 현위치가 방문했던 위치면 다음 큐
        if location in visited:
            continue
        # 다음 방문 시간이 지금 시간보다 빠를 수 없으므로 그냥 cnt
        visited[location] = cnt
        # 수빈이 현위치가 0이하면 X-1로 이동할 필요없음
        if 0 < location:
            queue.append([location - 1, cnt + 1])
        # 수빈이 현위치가 동생보다 크면 X+1로 이동할 필요없음
        if location < K:
            queue.append([location + 1, cnt + 1])
        # 수빈이 현위치가 동생 위치 2배보다 커지면 2*X로 이동할 필요없음
        if location < K * 2:
            queue.append([2 * location, cnt + 1])
print(sol())