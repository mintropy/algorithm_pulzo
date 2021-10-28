import sys
ipt = sys.stdin.readline

def sol():
    R, S = map(int, ipt().split())
    pic = []
    # 열별 유성의 가장 낮은 부분을 담는 배열
    meteor_low_part = [-1 for _ in range(S)]
    # 열별 땅의 가장 높은 부분을 담는 배열
    ground_high_part = [R for _ in range(S)]
    # 입력을 받을 때마다 열별로 유성의 가장 낮은 부분, 땅의 가장 높은 부분을 배열에 넣음
    for i in range(R):
        part = list(ipt().rstrip())
        for j in range(S):
            # 위에서부터 아래로 유성의 위치를 계속 갱신하여
            # 유성의 가장 낮은 부분을 판단
            if part[j] == 'X':
                meteor_low_part[j] = i
            # 최초로 땅을 확인한 부분을 배열에 넣는데 좀 비효율적인듯
            elif part[j] == '#':
                ground_high_part[j] = min(ground_high_part[j], i)
        pic.append(part)

    # 열별 유성과 땅의 높이차가 가장 낮은 것을 구함
    gap = R
    for j in range(S):
        if meteor_low_part[j] != -1:
            gap = min(ground_high_part[j] - meteor_low_part[j] - 1, gap)
    idx = max(meteor_low_part)

    # 유성의 가장 낮은 부분부터 시작하여 인덱스 0이 될 때까지
    # 유성을 찾아 높이차만큼 밑에 유성을 그리고
    # 기존 값에 빈 하늘을 덮어 씌움
    while idx >= 0:
        for j in range(S):
            if pic[idx][j] == 'X':
                pic[idx][j] = '.'
                pic[idx + gap][j] = 'X'
        idx -= 1

    # 리스트 최대 900만개 찍기 위해선 print() 보다 sys.stdout.write()가 더 효율적
    for i in range(R):
        for j in range(S):
            sys.stdout.write(pic[i][j])
        sys.stdout.write('\n')

sol()