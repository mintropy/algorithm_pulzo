'''
A → B

'''
import sys
input = sys.stdin.readline
from collections import deque

A, B = map(int,input().split())
# q 생성
q = deque([(A,0)])

# bfs
# 숫자가 작아지는 건 없기 때문에 작은 수들 중에서만
# 신경쓰는 방식을 사용
while q:
    # 숫자와 카운트
    num, cnt = q.popleft()

    # B에 도착하면 카운트 + 1하고 빠져나옴.
    if num == B:
        ans = cnt + 1
        break

    # 2배
    if num * 2 <= B:
        q.append((num*2,cnt+1))
    # 뒤에 1추가
    if int(str(num) + "1") <= B:
        q.append((int(str(num) + "1"),cnt+1))
# 없으면 -1
else:
    ans = -1
print(ans)