# 전체 가로, 세로  -> n * 2
# 쭉 보면서 goal과 같은 숫자가 더 많은 줄이 n 이상이면 된다 !?! => 안됨 ㅠ 로직..다시..

n, goal = map(int,input().split())

computers = list(list(map(int,input().split())) for _ in range(n))

for k in range(2):  # 2번만 바꿔주면 바뀔 것은 다 바뀌는 것이라고 함..(가로는 바뀐 세로의 영향도 받고, 세로는 바뀐 가로의 영향도 받고)
    # 가로
    for i in range(n):
        cnt = 0
        for j in range(n):
            if computers[i][j] == goal:
                cnt += 1
        if cnt > n//2:
            for j in range(n):
                computers[i][j] = goal
            

    # 세로
    for i in range(n):
        cnt = 0
        for j in range(n):
            if computers[j][i] == goal:
                cnt += 1
        if cnt > n//2:
            for j in range(n):
                computers[j][i] = goal

# 확인
def final_check():
    for i in range(n):
        for j in range(n):
            if computers[i][j] != goal:
                return False
    return True


if final_check():
    print(1)
else:
    print(0)