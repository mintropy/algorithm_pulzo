"""
Title : 즐거운 단어
Link : https://www.acmicpc.net/problem/2922
"""

def make_word(token: list, idx: int, count: int, l_find: bool):
    global total_count
    if idx == len(token):
        if l_find:
            total_count += count
        return
    # 해당 idx마다 본인 포함 왼쪽, 오른쪽으로 3칸 범위까지 확인
    # 만약 0, 1, n - 2, n - 1인 경우라면, 가능한 부분까지 확인
    # 해당 위치가 공백일때만 탐색
    if token[idx]:
        make_word(token, idx + 1, count, l_find)
    else:
        # 경우의 수
        # 1. 왼쪽 2개, 오른쪽 2개, 왼쪽/오른쪽으로 같은게 있는 경우
        #   같은 분류로 넣으면 3개 연속이 됨
        # 2. 해당 범위에 같은 경우가 없음
        #   어떤 분류가 들어가던지 상관 없음
        # 해당 범위에 자음 or 모음이 연속인지 확인
        check_left = set(('V', 'C'))
        check_mid = set(('V', 'C'))
        check_right = set(('V', 'C'))
        # 왼쪽으로 탐색
        if idx >= 2:
            if token[idx - 1] == 'V' and token[idx - 2] == 'V':
                check_left.remove('V')
            elif token[idx - 1] == 'C' and token[idx - 2] == 'C':
                check_left.remove('C')
        # 왼쪽 한칸/ 오른쪽 한칸
        # 오른쪽이 비어있으면 둘 다 추가
        if idx >= 1 and idx < len(token) - 1:
            if token[idx + 1]:
                if token[idx - 1] == 'V' and token[idx + 1] == 'V':
                    check_mid.remove('V')
                elif token[idx - 1] == 'C' and token[idx + 1] == 'C':
                    check_mid.remove('C')
        # 오른쪽 두 칸 확인
        # 둘 중 하나라도 비어있으면 둘 다 추가
        # 아니면 둘 다 비교
        if idx < len(token) - 2:
            if token[idx + 1] and token[idx + 2]:
                if token[idx + 1] == 'V' and token[idx + 2] == 'V':
                    check_right.remove('V')
                elif token[idx + 1] == 'C' and token[idx + 2] == 'C':
                    check_right.remove('C')
        # 가능한 경우 수 탐색
        # 1. check가 모두 2개씩 있는 경우 가능한 모든 경우로 처리
        # 2. check로 가능한게 한 종류가 하나인 경우 그것으로 처리
        # 3. check로 가능한게 한 종류가 둘 이상이면 조건 확인
        #   만약 그 종류가 같다면 그것으로 처리, 다르면 리턴
        
        left = sorted(check_left)
        mid = sorted(check_mid)
        right = sorted(check_right)
        if left == mid == right and len(left) == 2:
            # 모음으로
            token[idx] = 'V'
            make_word(token, idx + 1, count * 5, l_find)
            token[idx] = ''
            # L로
            token[idx] = 'C'
            make_word(token, idx + 1, count, l_find | True)
            token[idx] = ''
            # L제외 자음으로
            token[idx] = 'C'
            make_word(token, idx + 1, count * 20, l_find)
            token[idx] = ''
        else:
            # 2, 3 조건을 합쳐서 세 부분에서 가능한거만 추려서 확인
            able = check(left, mid, right)
            if len(able) == 2:
                return
            else:
                # 모음이 가능할 때
                if able[0] == 'V':
                    token[idx] = 'V'
                    make_word(token, idx + 1, count * 5, l_find)
                    token[idx] = ''
                # 자음이 가능할 때
                else:
                    # L일때와 아닐 때
                    # L로
                    token[idx] = 'C'
                    make_word(token, idx + 1, count, l_find | True)
                    token[idx] = ''
                    # L제외 자음으로
                    token[idx] = 'C'
                    make_word(token, idx + 1, count * 20, l_find)
                    token[idx] = ''


def check(left: list, mid: list, right: list) -> list:
    able = set()
    if len(left) == 1:
        able |= set(left)
    if len(mid) == 1:
        able |= set(mid)
    if len(right) == 1:
        able |= set(right)
    return list(able)


word = input().strip()
# 단어로 비교하는 대신 알파벳 별로 분류하여 처리
# 공백, L, 자음, 모음으로 분류
L_find = False
token = []
for alp in word:
    if alp in 'AEIOU':
        token.append('V')
    elif alp == '_':
        token.append('')
    elif alp == 'L':
        token.append('C')
        L_find = True
    else:
        token.append('C')

total_count = 0

make_word(token, 0, 1, L_find)

print(total_count)
