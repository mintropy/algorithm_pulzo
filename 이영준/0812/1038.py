"""
Title : 감소하는 수
Link : https://www.acmicpc.net/problem/1038
"""


def check(decreasing_num, num, num_len):
    str_list = list(str(num))
    # 두 자리씩 확인하며 감소하는 수가 아니면 False 반환
    for i in range(num_len - 1):
        if str_list[i] == '0':
            return False, i
        if not decreasing_num[int(''.join([str_list[i], str_list[i + 1]]))]:
            return False, i
    return True, 0


def search():
    n = int(input())
    
    # 두 자리수까지 감소하는 숫자인지 미리 저장
    decreasing_num = [False] * 100
    for i in range(10):
        decreasing_num[i] = True
    for i in range(1, 10):
        for j in range(i):
            decreasing_num[i * 10 + j] = True
    
    if n == 0:
        return 0
    
    count = 0
    for i in range(1, 100):
        if decreasing_num[i]:
            count += 1
        if count == n:
            return i
    
    decreasing_seq = list(map(str, range(9, -1, -1)))
    
    # 세자리수부터 탐색
    num_len = 3
    num = 210
    while num_len < 11:
        if num >= 10 ** num_len:
            num_len += 1
            num = int(''.join(decreasing_seq[-num_len:]))
        tf, idx =  check(decreasing_num, num, num_len)
        if tf:
            count += 1
            if count == n:
                return num
            num += 1
        # 감소하는 수가 아니면 모두 탐색을 해서 넘어갈 필요가 없음
        else:
            # 처음 감소가 아닌 부분에서 1을 더함
            # 65330 >> 65430
            num += 10 ** (num_len - idx -1)
            # 해당 부분 밑에는 가장 작은 감소하는 수로 초기화
            # 65330 >> 65430 >> 65410
            new_decreasing = int(''.join(decreasing_seq[-(num_len - idx - 1):]))
            num //= 10 ** (num_len - idx - 1)
            num *= 10 ** (num_len - idx - 1)
            num += new_decreasing
    return - 1

print(search())
