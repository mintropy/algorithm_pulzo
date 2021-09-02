N = int(input())

def sol(n):
    # 초기값 0, 반복문 진입 안함
    res = 0
    for _ in range(n):
        # 가능한 최대의 감소하는 수, 이 값을 초과하면 -1 반환
        if res == 9876543210:
            return -1
        # n - 1번째 감소하는 수를 쪼개서 담을 리스트
        arr = []
        # 값 보존을 위한 임시 변수
        temp = res
        # 쪼갬
        while temp:
            arr.append(temp % 10)
            temp //= 10
        # n - 1번째 수에서 가장 낮은 자리수부터 몇번째 자리수까지 연속적인가를 판단
        # 즉, 자리올림이 발생하는지, 몇번째 자리수까지 발생하는지를 확인하기 위함
        idx = 0
        # 1의 자리부터 최대 자리수까지 증가
        while idx < len(arr) - 1:
            # 다음 자리수와 연속이라면 인덱스를 증가
            if arr[idx + 1] - arr[idx] == 1:
                idx += 1
                continue
            # 아니라면 반복문을 탈출, 연속인 최대 자리수가 유지됨
            else:
                break
        # 인덱스가 증가하지 않았다면 자리올림이 발생하지 않는 경우, 그냥 1 증가
        if idx == 0:
            res += 1
        else:
            # 인덱스가 증가했다면 그 증가 구간의 최대 자리수에 1을  더함
            arr[idx] += 1
            # 만약 그 증가한 최대 자리수가 9를 초과한다면 자리수가 증가했다는 것을 의미
            if arr[idx] > 9:
                # 그 최대자리수에서 가능한 가장 작은 수로 바꿈
                arr = [i for i in range(idx + 2)]
            # 자리수가 증가하는 경우가 아니라면
            else:
                # 최대자리수를 제외하고 나머지 구간을 가장 작은 수로 바꿈
                for i in range(idx):
                    arr[i] = i
            # 배열을 다시 결과로 바꿈
            for i in range(len(arr)):
                temp += arr[i] * (10 ** i)
            res = temp
    return res
print(sol(N))
