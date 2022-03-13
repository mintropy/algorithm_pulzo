'''
우체국

'''
import sys
input = sys.stdin.readline

N = int(input())

# # 왼쪽인원
# # 오른쪽인원
# left_people = 0
# right_people = 0
# XA = []

# # 저장
# for _ in range(N):
#     X, A = map(int,input().split())
#     right_people += A
#     XA.append((X,A))
# # 정렬
# XA.sort()

# # 총거리 구하기
# distance = 0
# left_people += XA[0][1]
# right_people -= XA[0][1]
# for i in range(1,N):
#     distance += abs((XA[i][0] - XA[i-1][0])*XA[i][1])

# # 거리가 안줄어드는 곳 찾기
# for i in range(1,N):
#     if distance <= distance + (left_people - right_people)*(XA[i][0] - XA[i-1][0]):
#         print(XA[i-1][0])
#         break
#     # 왼쪽인원만큼 늘어나고 오른쪽인원만큼 줄어든다.
#     distance += (left_people - right_people)*(XA[i][0] - XA[i-1][0])
#     left_people += XA[i][1]
#     right_people -= XA[i][1]
# else:
#     print(XA[-1][0])
#######################################
# 왼쪽인원
# 오른쪽인원
left_people = 0
right_people = 0
XA = []

# 저장
for _ in range(N):
    X, A = map(int,input().split())
    right_people += A
    XA.append((X,A))
# 정렬
XA.sort()

# 인원의 중앙값 찾기
for i in range(N):
    left_people += XA[i][1]
    right_people -= XA[i][1]
    if left_people >= right_people:
        print(XA[i][0])
        break
