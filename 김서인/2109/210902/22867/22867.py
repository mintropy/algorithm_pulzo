import heapq
import sys

input = sys.stdin.readline

N = int(input())
buses = []
for _ in range(N):
    in_time, out_time = input().split()
    # 시각, 분, 초, 밀리초를 계산해서 하나의 숫자로 해준다.
    in_time_final = int(in_time[9:]) + int(in_time[6:8]) * 1000 + int(in_time[3:5]) * 100000 + int(
        in_time[:2]) * 10000000
    out_time_final = int(out_time[9:]) + int(out_time[6:8]) * 1000 + int(out_time[3:5]) * 100000 + int(
        out_time[:2]) * 10000000
    buses.append((in_time_final, out_time_final))

# 출발 시각 이른 것부터 정렬
buses.sort()

Q = []
heapq.heappush(Q, (buses[0][1], buses[0][0]))  # 나가는 시각, 들어오는 시각
bus_one_time = 1

for i in range(1, N):  # 하나씩 쭉 보기
    fast_out = heapq.heappop(Q)  # 가장 빨리 나가는 버스
    if buses[i][0] < fast_out[0]:  # 가장 빨리 나가는 버스가 나가는 시각보다, 이번에 들어오는 버스가 더 빨리 들어오면
        bus_one_time += 1  # 종점에 같이 있어야 하니까 하나 더함
        heapq.heappush(Q, fast_out)  # 가장 빨리 나가는 버스가.. 안 나갔으니까 더해줌
        heapq.heappush(Q, (buses[i][1], buses[i][0]))  # 이번 버스도 들어옴
    else:  # 가장 빨리 나가는 버스가, 이번에 들어오는 버스보다 빨리 나가면
        heapq.heappush(Q, (buses[i][1], buses[i][0]))  # 이번 버스 들어옴
print(bus_one_time)