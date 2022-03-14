import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    cities = list(tuple(map(int, input().split())) for _ in range(N))
    cities.sort()

    total_people_cnt = sum([x[1] for x in cities])
    cities_left_right_people = list([0] * 2 for _ in range(N))

    cities_left_right_people[0][1] = total_people_cnt - cities[0][1]

    ans_idx = 0
    ans_cnt = cities_left_right_people[0][1] - cities_left_right_people[0][0]

    for i in range(1, N):
        cities_left_right_people[i][0] = cities_left_right_people[i - 1][0] + cities[i-1][1]   # 그 마을 왼쪽의 사람들의 수
        cities_left_right_people[i][1] = cities_left_right_people[i - 1][1] - cities[i][1]  # 그 마을 오른쪽의 사람들의 수

        tmp = abs(cities_left_right_people[i][0] - cities_left_right_people[i][1])
        if ans_cnt > tmp:  # 그 마을의 좌우 사람들 수가 ans_cnt보다 적으면
            ans_cnt = tmp
            ans_idx = i

    print(cities[ans_idx][0])