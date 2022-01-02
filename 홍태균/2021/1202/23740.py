'''
버스 노선 개편하기

'''
import sys
input = sys.stdin.readline

N = int(input())

# 버스 노선 저장
bf_bus_list = []
for _ in range(N):
    bf_bus_list.append(list(map(int,input().split())))
# S를 기준으로 정렬
bf_bus_list.sort()

# 개편된 노선을 저장하기위한 리스트
# 처음 노선을 미리 저장
af_bus_list = [bf_bus_list[0][:]]

# 다음 노선부터 파악
for i in range(1,N):
    S, E, C = bf_bus_list[i][:]
    # 개편된 노선의 가장 마지막 노선의 E가 S보다 작다면 끊어진 것
    # 그렇기 때문에 새로운 노선을 만든다.
    if af_bus_list[-1][1] < S:
        af_bus_list.append([S,E,C])
    # 그렇지 않다면 이전의 노선과 이어질 수 있다.
    else:
        # 개편된 노선의 E는 더 긴 쪽을 택한다.
        if af_bus_list[-1][1] < E:
            af_bus_list[-1][1] = E
        # 개편된 노선의 C는 더 작은 쪽을 택한다.
        if af_bus_list[-1][2] > C:
            af_bus_list[-1][2] = C
# 길이 축력
print(len(af_bus_list))
# 노선 출력
for _list in af_bus_list:
    print(*_list)

