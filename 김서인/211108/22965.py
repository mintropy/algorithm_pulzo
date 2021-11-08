import sys

input=sys.stdin.readline

N=int(input())
arr = list(map(int,input().split()))

# k가 1인 경우(안 잘라도 되는 경우) -> 그 자체가 정렬되어 있는 경우
arr2 = sorted(arr)
if arr2 == arr:
    print(1)

# k가 2인 경우 -> 빙~ 돌아서 정렬되어 있는 경우(3 4 5 6 | 1 2,  4 5 6| 1 2 3처럼)

# 1 5  9 |2 3 4
else:
    min_value = min(arr)
    min_idx = arr.index(min_value)

    before = min_value

    flag= True
    for i in range(min_idx+1, N):
        if before > arr[i]:
            flag = False
            break
        else:
            before = arr[i]

    for i in range((min_idx+N)%N):
        if before > arr[i]:
            flag = False
            break
        else:
            before = arr[i]

    if flag == True:
        print(2)
    else:
        print(3)


