def new_num_sum(num:int):
    """
    숫자의 각 자리수에서 홀수의 개수를 리턴한다
    """
    new_num_total = 0
    while num:
        if (num % 10) % 2: # 홀수이면
            new_num_total += 1   
        num//=10
    return new_num_total


def sol(n: str, total: int): # 지금 수, 지금까지 홀수의 개수
    if len(n) == 1: # 수가 한 자리이면 종료
        makes.append(total) # 그때까지의 홀수의 개수를 리스트에 추가
        return
    
    elif len(n) == 2: # 수가 두 자리이면
        new_num = int(n[0]) + int(n[1]) # 2개로 나누고, 더해서 새로운 수로 생각하기
        sol(str(new_num), total + new_num_sum(new_num))

    else: # 수가 세 자리 이상이면
        for i in range(1, len(n)): # 자를 위치 2개
            for j in range(i+1, len(n)):
                part1 = n[:i]
                part2 = n[i:j]
                part3 = n[j:]

                new_num = int(part1) + int(part2) + int(part3) # 3개의 수로 나누고, 더해서 새로운 수로 생각하기
                sol(str(new_num), total + new_num_sum(new_num))

N = input()
makes =[]
sol(N, new_num_sum(int(N)))
print(min(makes), max(makes))