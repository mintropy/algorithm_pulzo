import sys

input = sys.stdin.readline

Q = int(input())
information_gorillas = {}
hosuk_information_value_sum = 0

for _ in range(Q):
    query = input().split()

    if query[0] == '1':  # 정보 얻은 고릴라 이름, 정보의 개수, 정보의 가치
        name = query[1]
        K = int(query[2])
        K_values = list(map(int, query[3:]))

        if information_gorillas.get(name):  # 이미 나온 적 있는 고릴라이면 추가된 정보관련 내용을 추가
            information_gorillas[name].extend(K_values)

        else:  # 처음 나온 고릴라이면
            information_gorillas[name] = K_values

    elif query[0] == '2':  # 호석이가 접촉한 고릴라, 호석이가 구매하는 정보의 개수
        name = query[1]
        B = int(query[2])

        # 그 고릴라가 있는지 체크
        if information_gorillas.get(name):
            # 있으면 정보 가치에 따라서 내림차순 정렬
            information_gorillas[name].sort(reverse=True)

            # B개 이하일 경우 정보 모두 구매, 고릴라 삭제
            if len(information_gorillas[name]) <= B:
                hosuk_information_value_sum += sum(information_gorillas[name])
                del information_gorillas[name]
            else:  # B게 보다 많다면
                # B개 정보를 구매하고
                hosuk_information_value_sum += sum(information_gorillas[name][:B])
                # 고릴라는 그 정보를 파기하기
                information_gorillas[name] = information_gorillas[name][B:]

print(hosuk_information_value_sum)
