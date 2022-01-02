'''
k개의 부분 배열

'''
import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int,input().split()))

# 무조건 한토막은 있기 때문
cnt = 1

for i in range(1,N):
    # 숫자가 줄어 들면 범위가 나뉘기 때문에
    # 1증가
    if nums[i-1] > nums[i]:
        cnt += 1
    # 3조각이면 무조건 3으로 가능하기 때문에 break
    if cnt == 3:
        break

if cnt == 1:
    print(1)
# 2 조각이지만 만약 섞여있는 경우면 2개로 불가능 
elif cnt == 2 and nums[0] > nums[N-1]:
    print(2)
else:
    print(3) 


## 77
# import sys
# input = sys.stdin.readline

# N = int(input())

# nums = list(map(int,input().split()))


# cnt = 1

# num = minnum = nums[0]

# for i in range(1,N):
#     if num > nums[i]:
#         cnt += 1
#         if minnum < nums[i]:
#             cnt += 1
#     num = nums[i]
#     if cnt == 3:
#         break

# if cnt == 1:
#     print(1)
# elif cnt == 2:
#     print(2)
# else:
#     print(3) 

## 69
# import sys
# input = sys.stdin.readline

# N = int(input())

# nums = list(map(int,input().split()))


# cnt = 1

# num = minnum = nums[0]

# for i in range(1,N):
#     if num > nums[i]:
#         cnt += 1
#     num = nums[i]


# if cnt == 1:
#     print(1)
# elif cnt == 2:
#     print(2)
# else:
#     print(3) 