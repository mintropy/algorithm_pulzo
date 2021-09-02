import sys

def sol():
    # 입력
    N, K = map(int, sys.stdin.readline().split())
    dolls = list(map(int, sys.stdin.readline().split()))
    # 라이언의 총 개수가 K개 보다 적으면 -1
    if dolls.count(1) < K:
        return -1
    # 시작 포인터를 첫 번째 라이언 위치로
    s_p = dolls.index(1)
    # K번째 라이언의 위치를 찾기 위한 과정
    next_one_idx = s_p
    # 첫 번재 라이언을 카운트
    cnt = 1
    # 카운트가 K가 될 때까지
    while cnt < K:
        # 다음 라이언을 찾으며
        next_one_idx = dolls.index(1, next_one_idx + 1)
        # 카운트 += 1
        cnt += 1
    # K번째 라이언을 끝 포인터에 넣고 반환값에 포인터의 차를 넣는다.
    e_p = next_one_idx
    res = e_p - s_p + 1
    # 반환값이 K와 같다면 리턴
    if res == K:
        return K
    # 끝 포인터가 N과 같아지기 전까지 루프
    while e_p < N:
        # if res == K:
        #     return K
        # 초기값에서 시작점과 끝점포함 그 사이에 K개의 라이언이 있음을 확인했으므로 추가 확인 불필요
        if dolls[s_p] == 1 and dolls[e_p] == 1:
            res = min(res, e_p - s_p + 1)
            s_p += 1
            e_p += 1
            continue
        if dolls[s_p] == 2:
            s_p += 1
        if dolls[e_p] == 2:
            e_p += 1
    return res
# 함수실행과 출력
print(sol())
