import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 후보수 C, 유권자수 V
    C, V = map(int, input().split())
    cnt = [0] * (C+1)
    prefer_list = []
    prefer_dict = []
    for v in range(V):
        v = list(map(int, input().split()))
        prefer_list.append(v)
        # 인덱스가 작을수록 선호도가 높음
        prefer_dict.append({n: i for i, n in enumerate(v)})

    # 후보자가 1명인 경우
    if C == 1:
        print(1, 1)
        continue

    # 1차 투표
    for v in prefer_list:
        cnt[v[0]] += 1

    # 1차 투표 결과 (후보자가 2명인 경우 1차 투표에서 승부가 남)
    cnt = [(i, n) for i, n in enumerate(cnt)]
    cnt.sort(key=lambda x:-x[1])
    if cnt[0][1] > V//2: # 1등이 과반수 이상
        #print('1등이 과반수 이상입니다.')
        print(cnt[0][0], 1)
        continue
    else: # 1등이 과반수 넘지 못했을때
        # 1, 2등 후보를 a, b 에 각각 저장
        a, b = cnt[0][0], cnt[1][0]
        a_cnt, b_cnt = 0, 0
        for v in prefer_dict:
            if v[a] < v[b]:
                a_cnt += 1
            else:
                b_cnt += 1
        if a_cnt > b_cnt:
            print(a, 2)
        else:
            print(b, 2)
        continue