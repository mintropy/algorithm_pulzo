'''
세 용액

'''
import sys

input = sys.stdin.readline

N = int(input())

solutions = list(map(int,input().split()))

solutions.sort()

answer = []
diff = 10**10

for i in range(N-2):
    # 처음 용액 저장
    one = solutions[i]
    # 2번째, 3번째 용액 구하기
    st, ed = i+1, N-1
    while st < ed:
        two, three = solutions[st], solutions[ed]
        # 용액 합
        sum_sol = one + two + three
        # 현재의 차이보다 작으면 갱신
        if diff > abs(sum_sol):
            answer = [one,two,three]
            diff = abs(sum_sol)
        
        # 합이 양수면 줄여야 하기 때문에 끝을 줄인다
        if sum_sol > 0:
            ed -= 1
        # 합이 음수면 늘려야 하기 때문에 시작을 늘린다
        elif sum_sol < 0:
            st += 1
        # 0이면 최소이기 때문에 끝
        else:
            break
    
    if sum_sol == 0:
        break

# while st < ed:
#     # print(st,ed)
#     one, three = solutions[st], solutions[ed]
#     for i in range(st+1,ed):
#         two = solutions[i]
#         sum_sol = one + two + three
#         if diff > abs(sum_sol):
#             answer = [one,two,three]
#             diff = abs(sum_sol)
    
#     if sum(answer) >= 0:
#         ed -= 1
#     else:
#         st += 1

for i in range(3):
    print(answer[i],' ')

'''
4
-5 2 3 4

'''