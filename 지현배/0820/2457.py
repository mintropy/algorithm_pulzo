import sys
input = sys.stdin.readline
def sol():
    N = int(input())
    flowers = [list(map(int, input().split())) for _ in range(N)]
    flowers.sort(key=lambda x: (x[2], x[3], x[0], x[1]))
    target = [12, 1]
    idx = N - 1
    res = 0
    early = [12, 32]
    while idx >= 0:
        # 타겟이 현재의 개화 이후, 낙화 이전인지 확인한다.
        # 만족한다면 early를 갱신하고 넘어간다.
        if (flowers[idx][0] < target[0] or (flowers[idx][0] == target[0] and flowers[idx][1] <= target[1])) and (target[0] < flowers[idx][2] or (target[0] == flowers[idx][2] and target[1] <= flowers[idx][3])):
            # early를 더 이른 것으로 갱신
            if flowers[idx][0] < early[0] or (flowers[idx][0] == early[0] and flowers[idx][1] <= early[1]):
                early = [flowers[idx][0], flowers[idx][1]]
        # 만족하지 않는다면 우선 early가 현재의 개화 이후, 낙화 이전인지 확인한다.
            # 만족한다면 타겟에 얼리를 넣고 얼리에 스타트를 넣는다. 그리고 카운트를 늘린다.
        elif (flowers[idx][0] < early[0] or (flowers[idx][0] == early[0] and flowers[idx][1] <= early[1])) and (early[0] < flowers[idx][2] or (early[0] == flowers[idx][2] and early[1] <= flowers[idx][3])):
            target = early
            early = [flowers[idx][0], flowers[idx][1]]
            res += 1
        idx -= 1
        # 끝까지 순회하기 전에 target이 3.1 이하라면 최소 개수를 다 구한 것이므로 res를 반환한다.
        if target[0] < 3 or (target[0] == 3 and target[1] == 1):
            return res
    # while문이 끝났을때의 얼리가 3.1 이전이라면 결과에 1을 더해서 반환한다.
    if early[0] < 3 or (early[0] == 3 and early[1] == 1):
        return res + 1
    # 3.1 이후라면 공백이 생기므로 return 0
    else:
        return 0
print(sol())
'''
4
1 1 5 31
1 1 6 30
5 15 8 31
6 10 12 10
2

10
2 15 3 23
4 12 6 5
5 2 5 31
9 14 12 24
6 15 9 3
6 3 6 15
2 28 4 25
6 15 9 27
10 5 12 31
7 14 9 1
5

1
3 2 12 1
0

1
3 1 11 30
0

3
3 1 5 5
5 5 10 8
10 7 11 30
0

3
1 1 11 30
11 10 12 5
3 1 12 1
1

11
2 28 8 16
6 18 7 9
9 5 10 25
4 22 8 25
5 22 6 13
8 18 9 16
4 29 10 4
8 23 11 25
6 26 12 1
3 3 10 19
8 3 10 11
2

10
1 1 11 23
11 22 11 24
11 23 11 25
11 24 11 26
11 25 11 27
11 26 11 28
11 27 11 29
11 28 12 1
11 23 11 27
11 27 12 1
3

3 
1 1 7 10 
7 10 7 11 
7 10 12 31 
2

2 
3 1 3 2 
3 2 12 1 
2

2 
3 1 11 30 
11 30 12 1 
2

3
1 1 11 30
11 10 12 5
3 1 12 1
1
'''