'''
자리수로 나누기

'''
import sys
input = sys.stdin.readline

input_num = input().strip()
# 포함되어 있는 숫자 종류
num_set = set(map(int,input_num))
# 0은 제거
if 0 in num_set:
    num_set.remove(0)

# 자릿수를 늘리기 위해서
idx = 1
# 종료하기 위해서
flag = False

# 그 자체로 가능할 때
for num in num_set:
    now_num = int(input_num)
    if now_num % num:
        break
else:
    flag = True

# 가능하지 않으면 숫자를 추가하기
if not flag:
    while 1:
        # 10**idx 만큼 뒤에 붙여서
        for i in range(10**idx):
            # 숫자 만들기
            now_num = int(input_num + str(i).zfill(idx))
            
            # 확인하기
            for num in num_set:
                if now_num % num:
                    break
            else:
                flag = True
                break
        # 인덱스 증가와 확인하기   
        idx += 1
        if flag:
            break

print(now_num)