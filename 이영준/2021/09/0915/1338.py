"""
Title : 알 수 없는 번호
Link : https://www.acmicpc.net/problem/1338
"""

# st, end 입력에 대한 조건 없음
# x, y입력에 대한 조건 없음

st, end = map(int, input().split())
if st > end:
    st, end = end, st
x, y = map(int, input().split())
if x < 0:
    x *= -1

# 나머지가 나누는 수 보다 크거나 같을 때
if y >= x or y < 0:
    print('Unknwon Number')
else:
    # 만족하는 수 찾기
    m = (st // x) * x + y
    if m < st:
        m += x
    # 없는 경우
    if m > end:
        print('Unknwon Number')
    elif (st <= m <= end):        
        # 하나 더 존재할 수 있는 경우
        if (st <= m + x <= end):
            print('Unknwon Number')
        else:
            print(m)


'''
Counter Example
-10 -4
-7 2
ans : -5

10 15
-7 6
'''