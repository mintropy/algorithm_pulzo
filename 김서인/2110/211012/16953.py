import collections
import sys

input = sys.stdin.readline

A, B = map(int, input().split())

# 방문 체크 할 필요는 없을 듯(2를 곱한다고 오른쪽에 1추가한 수가 되진 않을 거라서)
# 연산의 최솟값을 찾으려고 하니까 BFS

q = collections.deque()
q.append((A, 0))
while q:
    tmp, cnt = q.popleft()
    if tmp == B:  # 정답이면
        print(cnt + 1)
        break
    else:
        if tmp * 2 <= 10 ** 9:
            q.append((tmp * 2, cnt + 1))

        if tmp + tmp <= 10 ** 9:
            q.append(((tmp*10+1), cnt + 1))


else:
    print(-1)

# B가 A보다 클 동안
# B를 줄여가면서(나누기 10한 나머지가 1인지, 2로 나누어 떨어지는지 보고 나서 가능하면 그 처리를 한다.)
# A가 되는지 보는 방식의 코드로도 많이 짜신 것 같다. 더 빠르다.