'''
1루수가 누구야

'''
import sys
input = sys.stdin.readline

# 사람을 저장 
# 숫자로 인덱스 받기위해 0 인덱스를 없애기 위해서
people = [-1]
for _ in range(9):
    num, A = map(int,input().split())
    people.append((num, A))

# 답이 될 수 있는 걸 다 담기 위해서
result = []
# 1~9번까지 거짓말 하는 사람
for i in range(1,10):
    # 1루수인사람을 찾기 위해
    num_list = [-1] * 10
    flag = 0
    # 1~9까지 확인
    for j in range(1,10):
        # 거짓말하는 사람이면 바꿔서
        if i == j :
            num, A = people[j]
            num = 1-num
        else:
            num, A = people[j]
        # 1이면 추가
        if num:
            # 이미 제외되었다면 모순이기 때문에
            # 다음 숫자로 넘어가기
            if num_list[A] == 0:
                flag = 1
                break
            num_list[A] = 1
        # 0이면 제외
        else:
            # 이미 추가되었다면 모순이기 때문에
            # 다음 숫자로 넘어가기
            if num_list[A] == 1:
                flag = 1
                break
            num_list[A] = 0
    # 모순이 일어나면 바로 다음으로
    if flag:
        continue
    
    # 다 순회하고나서 대상이 1명이라면 결과에 추가
    if num_list.count(1) == 1:
        result.append(num_list.index(1))
    # 아닌 대상이 8명이라면 나머지 한명 추가
    elif num_list.count(0) == 8:
        result.append(num_list.index(-1,1))
    # 1이 없다면 여러 명이 결과에 추가되기 때문에 
    # 이 경우는 결국 -1이기 때문에
    # re를 초기화하고 탐색을 종료
    elif 1 not in num_list:
        result = []
        break

# 다 돌고나서 결과가 1명이라면 그 한명이 정답
if len(set(result)) == 1:
    print(result[0])
# 없거나 여러명이라면 -1
else:
    print(-1)
