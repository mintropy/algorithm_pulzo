n, k = map(int,input().split())
dolls = list(map(int,input().split()))

set_size = 10**6 # 라이언 k개 있는 가장 작은 연속된 인형 집합 크기/ 숫자를 저걸로 한 이유- 이게 n의 최댓값이니까
interval_cnt = 0 # 라이언 인형 갯수
end = 0

# 시작점이 1씩 증가함. 그 안에서 라이언 갯수가 k에 이를 때(혹은 끝 부분이 범위 초과할 때)까지 끝점도 1씩 증가. 

for start in range(n): # 시작점을 하나씩 증가
    while interval_cnt < k and end < n: # 라이언 인형을 k개만큼 못 찾았고, 끝부분이 범위 내에 있다면 
        if dolls[end] == 1: # 라이언 인형 찾았으면
            interval_cnt += 1 #내부 갯수 1증가
        end += 1 #끝점 1 증가

    # 라이언 인형을 k개 찾았거나, 끝부분이 범위 넘었으면 while 문 종료
    if interval_cnt == k: # 라이언 인형 k개 찾았으면 
        if set_size > (end - start): # 지금까지 라이언 k개 있는 가장 작은 연속된 인형 집합 크기와 비교해서
            set_size = (end - start) # 더 작은 값을 set_size에 대입

    if dolls[start] == 1:  # 만약에 start에서 라이언 찾았었으면 
        interval_cnt -= 1 # 라이언 인형 갯수 1 빼기 (이제 start에 1 더해서 다시 for문 돌릴 거니까)


if set_size == 10**6: # 라이언이 k개 이상이 되는 집합이 없다면
    print(-1)
else:
    print(set_size)