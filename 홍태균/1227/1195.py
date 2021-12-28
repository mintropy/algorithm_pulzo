'''
킥다운

'''
import sys
input = sys.stdin.readline

part1 = list(input().strip())
part2 = list(input().strip())

# 길이 비교
if len(part1) >= len(part2):
    long_part = part1
    short_part = part2
else:
    long_part = part2
    short_part = part1

# 한칸씩 앞으로 가면서 확인하기 위해서 빈칸은 0으로
check_part = ['0'] * (len(short_part) - 1) + long_part[:] + ['0'] * (len(short_part) - 1)

total_len = len(short_part) + len(long_part)
# 몇번째에서 시작하는지
index = -1
# 최소 길이 
result = total_len

# 작은 파트가 왼쪽에 있을 때
for i in range(len(short_part) - 1):
    # 한 칸씩 앞으로
    index += 1
    # 길이는 줄어듦
    total_len -= 1
    # 맞물림 확인
    for j in range(len(short_part)):
        # 둘다 이 면 맞물릴 수 없기 떄문에
        if check_part[index + j] == '2' and short_part[j] == '2':
            break
    # 맞물리는 경우 길이 확인
    else:
        if result > total_len:
            result = total_len

total_len -= 1
# 작은 파트가 큰 파트내에 있을 때
for i in range(len(long_part) - len(short_part) + 1):
    index += 1
    # 길이는 줄어들지 않고 긴 파트에 고정되기 떄문에

    for j in range(len(short_part)):
        if check_part[index + j] == '2' and short_part[j] == '2':
            break
    else:
        if result > total_len:
            result = total_len

# 작은 파트가 오른쪽으로 갈 때
for i in range(len(short_part) - 1):
    index += 1
    # 길이는 늘어남
    total_len += 1
    for j in range(len(short_part)):
        if check_part[index + j] == '2' and short_part[j] == '2':
            break
    else:
        if result > total_len:
            result = total_len

print(result)