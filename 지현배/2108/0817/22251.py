def sol():
    N, K, P, X = map(int, input().split())
    # 1층부터 N층까지
    # 최대 K자리수 0으로 시작 가능
    # 최소 1개 최대 P개 반전
    # 실제로는 X층
    # 7 segments
    segments = [
        0b1110111, 0b0100100, 0b1011101, 0b1101101, 0b0101110,
        0b1101011, 0b1111011, 0b0100101, 0b1111111, 0b1101111
    ]
    # 현재 위치를 리스트로 만든다
    curr = []
    while X:
        curr.append(X % 10)
        X //= 10
    # K 자리수까지 0으로 채운다
    if len(curr) < K:
        curr.extend([0 for _ in range(K - len(curr))])
    def DFS(i, floor, cnt):
        tmp = 0
        # 종료 조건 : 인덱스가 자리수를 넘어가면
        if i >= K:
            # 층이 가능한 층인지 확인한다
            if 0 < floor <= N:
                return 1
            else:
                return 0
        # 자리수가 다 안찼는데도 가능한 범위를 넘어갈 수 있다
        if floor > N:
            return 0
        for n in range(10):
            # XOR 연산으로 세그먼트가 몇 개 바뀌는지 확인한다
            ch_sgmts = segments[curr[i]] ^ segments[n]
            ch_cnt = 0
            # 바이너리 값을 카운트한다
            while ch_sgmts:
                ch_cnt += ch_sgmts & 1
                ch_sgmts >>= 1
            # 반전할 세그먼트 개수가 유효한지 확인한다
            if cnt >= ch_cnt:
                tmp += DFS(i + 1, floor + n * (10 ** i), cnt - ch_cnt)
        return tmp
    # 아무것도 변하지 않는 경우를 뺀다
    res = DFS(0, 0, P) - 1
    return res
print(sol())