# 빼기는 할 필요 없다. (빼기하면 0이 되는데, 0이 되면 나누기 못함. 더하기, 곱하기, 빼기해도 0)

import collections
import math

s, t = map(int, input().split())

if s == t:
    print(0)
elif t == 1:
    print('/')  # / 하면 되니까
else:
    visited = set()
    q = collections.deque()
    q.append((s, ''))
    while q:
        tmp, tmp_method = q.popleft()

        if tmp == t:  # 정답이면
            print(tmp_method)
            break
        else:
            if tmp * tmp <= 10**9 and tmp * tmp not in visited:
                q.append((tmp * tmp, tmp_method + '*'))
                visited.add(tmp * tmp)
            if tmp + tmp <= 10**9 and tmp + tmp not in visited:
                q.append((tmp + tmp, tmp_method + '+'))
                visited.add(tmp + tmp)
            if tmp / tmp not in visited:
                q.append((tmp / tmp, tmp_method + '/'))
                visited.add(1)
    else:
        print(-1)

#
# elif math.log(t, 2) == int(math.log(t, 2)):  # 2의 제곱수
#     cnt = 0
#     n = 2
#     while True:
#         n = n * n
#         cnt += 1
#         if n == t:
#             break
#
#     print('/' + '+' + '*' * cnt)
# else:
#     print(-1)
