import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


# build - segment tree 생성(루트부터 아래로 반씩 나누면서)
def build(arr, node, nodeleft, noderight):
    if nodeleft == noderight:  # 리프 노드- 범위에 노드가 하나니까 그걸 넣으면 됨.
        segment_tree[node] = arr[nodeleft]
        return segment_tree[node]

    # 범위에 노드가 두 개 이상이면
    mid = int((nodeleft + noderight) / 2)
    left_value = build(arr, node * 2, nodeleft, mid)  # 왼쪽 노드
    right_value = build(arr, node * 2 + 1, mid + 1, noderight)  # 오른쪽 노드

    segment_tree[node] = left_value + right_value
    return segment_tree[node]


# 구간 지정 -> 합 구하기
def total_sum(left, right, node, nodeleft, noderight):
    if right < nodeleft or noderight < left:  # 범위 아예 바깥에 있는 노드들
        return 0  # 그냥 무시

    if left <= nodeleft and noderight <= right:  # 노드가 범위에 완전히 포함됨.
        return segment_tree[node]

    # 범위가 노드에 걸친다. (쪼개져서 내려감.)
    mid = int((nodeleft + noderight) / 2)
    return total_sum(left, right, node * 2, nodeleft, mid) + total_sum(left, right, node * 2 + 1, mid + 1, noderight)


# 값 업데이트
def update(index, newvalue, node, nodeleft, noderight):
    if index < nodeleft or noderight < index:  # 값 변경되는 리프와 상관없는 노드(범위 밖)
        return segment_tree[node]  # 그대로 값 리턴(업데이트 안 일어남)

    if nodeleft == noderight:  # 값 변경될 리프
        segment_tree[node] = newvalue  # 업데이트
        return segment_tree[node]

    mid = int((nodeleft + noderight) / 2)
    left_value = update(index, newvalue, node * 2, nodeleft, mid)
    right_value = update(index, newvalue, node * 2 + 1, mid + 1, noderight)
    segment_tree[node] = left_value + right_value
    return segment_tree[node]


# 입력 받기
N, Q = MIIS()

arr = list(MIIS())

# 세그먼트 트리 만들기
segment_tree = [0] * (N * 4 + 1)
build(arr, 1, 0, N - 1)

# 명령 수행
for _ in range(Q):
    x, y, a, b = MIIS()
    if x > y:
        x, y = y, x
    print(total_sum(x - 1, y - 1, 1, 0, N - 1))
    update(a - 1, b, 1, 0, N - 1)
