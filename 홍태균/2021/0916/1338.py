'''
알 수 없는 번호
'''
'''
1. 입력되는 범위가 l > r일 수 있습니다 (swap 필요)

2. y가 0 <= y < |x| 범위가 아닐 수 있습니다. (이 경우엔 Unknwon Number 출력)

3. Unknown이 아닌 "Unknwon"을 출력해야 합니다

+) t를 x로 나눈 나머지 r (0 <= r < |x)를 구할 땐 r = (t % x + x) % x을 이용하시면 편합니다.
'''

import sys

st, ed = map(int,sys.stdin.readline().split())
# 1번 경우를 위해서
if st>ed:
    st, ed = ed, st

X, Y = map(int,sys.stdin.readline().split())
# X가 마이너스나 플러스나 상관 없으나 나의 방법에서 다음 수를 구하기 때문에 양수로 변환
X = abs(X)

# 2번 경우를 위해서
if 0<= Y < X:
    pass
else:
    print("Unknwon Number")
    exit()

# 처음 해당 숫자
first = st + Y - st % X 
# 두번째 해당 숫자
second = first + X

# 처음 숫자가 범위 안
if st <= first <= ed:
    # 처음 숫자와 두번째 숫자가 다있으면 못찾음
    if st <= second <= ed:
        ans = "Unknwon Number"
    else:
        ans = first
# 처음 숫자가 범위 안에 안들어오면
else:
    ans = "Unknwon Number"
print(ans)