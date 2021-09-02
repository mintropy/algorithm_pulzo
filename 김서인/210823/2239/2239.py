# https://dct-wonjung.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-%EC%8A%A4%EB%8F%84%EC%BF%A0 를 참고

def dfs(depth):  # 0이었던 것 중에 depth 번째 꺼를 채워줄 차례
    global end_flag

    if end_flag:  # 처음으로 스토쿠 완성 되었으면, 앞으로는 무조건 리턴
        return

    if depth == len(blanks):  # 스토쿠 완성
        end_flag = True
        for s in sdoku:
            print(''.join(map(str, s)))
        return

    ii, jj = blanks[depth]  # 채워야 할 빈 칸

    # 1~9 숫자 중 가로, 세로, 작은 사각형 안에 있는 숫자를 체크
    check = [True] + [False for _ in range(9)]
    for k in range(9):
        # 가로
        check[int(sdoku[ii][k])] = True  # 이미 1이어도 1로 해줘도 상관없고, 0이었으면 1로 바꿔주는 거
        # 세로
        check[int(sdoku[k][jj])] = True

    # 작은 사각형
    for k_i in range(3):
        for k_j in range(3):
            check[int(sdoku[(ii // 3) * 3 + k_i][(jj // 3) * 3 + k_j])] = True

    # print(ii,jj, check)
    # 가로, 세로, 작은 사각형에 없는 숫자를 대입하기
    for k in range(10):
        if check[k] == False:
            sdoku[ii][jj] = k
            dfs(depth + 1)
    sdoku[ii][jj] = '0'


sdoku = list(list(input()) for _ in range(9))
blanks = []  # 채워야 할 것들
end_flag = False
for i in range(9):
    for j in range(9):
        if int(sdoku[i][j]) == 0:
            blanks.append((i, j))
# print(blanks)
dfs(0)
