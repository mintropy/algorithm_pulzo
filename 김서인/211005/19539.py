N = int(input())
target_tree_height = list(map(int, input().split()))

# 사과나무들의 높이를 다 합치면 꼭 3의 배수가 되어야 함 (물 뿌리개로 1, 2를 줘서 한 턴에 전체적으로 3씩 성장시키니까..)
if sum(target_tree_height) % 3:
    print('NO')
else:
    # 물 뿌리개로 1 주는 것, 2 주는 것의 횟수가 같아야 함.
    # 2는 1+1로도 표현할 수 있음.
    # 물 뿌리개로 1 주는 최소 횟수 == 2 줄 수 있는 횟수 이면 정답
    # > 는 정답 불가능
    # < 이면 2로만 이뤄진 횟수가 3의 배수인지 체크

    # 물 뿌리개로 1 주는 최소 횟수 구하기
    tree_need_one = 0
    tree_can_two = 0
    for i in range(N):
        if target_tree_height[i] % 2:
            tree_need_one += 1
        tree_can_two += target_tree_height[i] // 2

    if tree_need_one > tree_can_two:  # 2를 쓸 수 있는 횟수보다 1을 써야 하는 횟수가 많으면
        print('NO')
    elif tree_need_one == tree_can_two:  # 그 횟수가 같으면 답
        print('YES')
    elif tree_need_one < tree_can_two and (
            tree_can_two - tree_need_one) % 3 == 0:  # 2를 쓸 수 있는 횟수가 1을 써야 하는 횟수보다 많고, 그 차가 3의 배수이면(1, 2로 나눌 수 있으니까)
        print('YES')

'''
6
1 1 1 4 3 2
-> 1을 필수로 4개는 써야 함
2는 최대 4개 쓸 수 있음. 이 둘이 같으면 답이 됨.


6
10000 1000 100 
-> 1을 필수로 0개는 써야 함.
2는 최대 5000+500+50 = 5550개
5550은 3의 배수
2만큼 주는 물 뿌리개, 2만큼 주는 물 뿌리개, 2만큼 주는 물 뿌리개 => 1만큼 주는 물 뿌리개, 2만큼 주는 물뿌리개, 1만큼~, 2만큼~ 으로 바꿀 수 있어서 문제 조건 만족



'''