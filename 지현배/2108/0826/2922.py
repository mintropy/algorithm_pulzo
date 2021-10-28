import sys
input = sys.stdin.readline
def sol():
    # L 포함 여부
    include_L = False
    # _의 인덱스를 담을 배열
    underbar = []
    vowels = ["A", "E", "I", "O", "U"]
    # 결과값
    res = 0
    # 인덱스 에러 방지 패딩
    data = [4, 4]
    string = input().rstrip()
    for i in range(len(string)):
        s = string[i]
        # "L"이면 L 포함됨을 확인하고 자음 판정하여 데이터에 넣는다.
        if s == "L":
            include_L = True
            data.append(1)
        # "_"이면 그 인덱스를 저장하고 빈칸 판정하여 데이터에 넣는다.
        elif s == "_":
            underbar.append(i + 2)
            data.append(0)
        # 모음이면 모음 판정
        elif s in vowels:
            data.append(2)
        # 나머지는 그냥 자음 판정
        else:
            data.append(1)
    # 다시 데이터 뒤쪽 패딩
    data += [4, 4]
    # 이미 3연속 자모음이 나왔으면 0
    for i in range(2, len(data) - 4):
        if (data[i] == data[i + 1] == data[i + 2] and data[i] != 0):
            return 0
    # 왼쪽 두칸 혹은 왼쪽 오른쪽 한칸씩 혹은 오른쪽 두칸이 k와 같은지 확인한다.
    def check(data, i, k):
        if (not ((data[i - 2] == data[i - 1]) and (data[i - 2] == k)) and\
            not ((data[i - 1] == data[i + 1]) and (data[i - 1] == k)) and\
            not ((data[i + 1] == data[i + 2]) and (data[i + 1] == k))):
            return True
        else: return False
    def DFS(idx, L, n):
        # 종료 조건: 끝까지 왔을 때 L 포함하고 있으면 결과에 더한다.
        if idx >= len(underbar):
            if L == True:
                nonlocal res
                res += n
            return
        i = underbar[idx]
        # 자음 넣을수 있는지 확인하고 L 아닌 자음 넣거나 L 넣기
        if check(data, i, 1) == True:
            data[i] = 1
            DFS(idx + 1, L, n * 20)
            DFS(idx + 1, True, n)
            data[i] = 0
        # 모음 넣을 수 있는지 확인하고 모음 넣기
        if check(data, i, 2) == True:
            data[i] = 2
            DFS(idx + 1, L, n * 5)
            data[i] = 0
    DFS(0, include_L, 1)
    return res
print(sol())