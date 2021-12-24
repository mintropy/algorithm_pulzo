import sys

input = sys.stdin.readline

part1 = input().strip()
part2 = input().strip()

if len(part1) > len(part2):
    part1, part2 = part2, part1
    # 1이 짧은 기어가 되게 함.

meet_thing = 0
for k in range(len(part1)):
    # 짧은 게 앞에서부터 출발해서, 한칸씩 겹쳐보면서 맞물리는지 보기.
    for i in range(k+1):
        if part1[-k+i-1] == '2' and part2[i] == '2':  # 둘 다 '이'(나온 부분)면 맞물리지 않는다는 뜻
            break
    else:  # 맞물리면
        meet_thing = max(meet_thing, k + 1)  # 맞물리는 갯수 업데이트

    # 짧은 게 뒤에서부터 출발해서, 한칸씩 겹쳐보면서 맞물리나 보기
    for i in range(k+1):
        if part1[i] == '2' and part2[-k+i-1] == '2':  # 둘 다 '이'(나온 부분)면 맞물리지 않는다는 뜻
            break
    else:  # 맞물리면
        meet_thing = max(meet_thing, k + 1)  # 맞물리는 갯수 업데이트

# 짧은 게 긴 거랑 만나는 지점 앞에서부터 출발해서, 한칸씩 앞으로 가면서 맞물리는지 보기-> 하나라도 ok되면 긴 것 길이가 정답
for k in range(len(part2) - len(part1) + 1):
    for i in range(len(part1)):
        if part1[i] == '2' and part2[i + k] == '2':  # 둘 다 '이'(나온 부분)면 맞물리지 않는다는 뜻
            break
    else:  # 맞물리면
        meet_thing = max(meet_thing, len(part1))  # 맞물리는 갯수 업데이트
        break  # 하나라도 되면 그만 봐도 됨(어차피 정답은 part2 길이)

print(len(part1) + len(part2) - meet_thing)
