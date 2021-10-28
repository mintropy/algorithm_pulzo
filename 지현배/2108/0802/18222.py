k = int(input())

# k번째 카드의 인덱스는 k-1
target = k - 1
# target을 4진수로 나타낼 리스트
quat = []
num = 0
# target을 4진수로 변환함, 뒤로 갈수록 큰 자릿수
while target:
    quat.append(target % 4)
    target //= 4

# 이전 시퀀스에서 0이냐 1이냐에 따라 다음 탐색 리스트가 변화함
string0 = [0, 1, 1, 0]
string1 = [1, 0, 0, 1]
res = 0
# 일단 0으로 시작
next_string = string0
while quat:
    # 4진수로 나타냈을 때 가장 큰 자릿수부터 시작
    idx = quat.pop()
    # 4진 값에 따라 결과값 도출
    res = next_string[idx]
    # 그 값에 따라 다음 시퀀스의 탐색 리스트 결정
    if res == 0:
        next_string = string0
    else:
        next_string = string1

print(res)