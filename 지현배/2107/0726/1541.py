# 입력
exp = input()
# 문자열에서 가장 빨리 나오는 '-' 연산자를 찾는다.
f = exp.find('-')
# 문자열 내에 '-' 연산자가 없으면
if f == -1:
    # 그대로 계산된 결과값을 출력한다.
    print(sum(list(map(int, exp.replace('+', ' ').replace('-', ' ').split()))))
# 문자열 내에 '-' 연산자가 있으면
else:
    # 그 첫번째 '-' 연산자 기준 앞과 뒤로 나누어
    # 앞 부분의 계산 결과값에서
    # 뒷 부분의 각 수의 절대값을 더한 값을 뺀다.
    front = sum(list(map(int, exp[0:f].replace('+', ' ').split())))
    back = sum(list(map(int, exp[f:].replace('-', ' ').replace('+', ' ').split())))
    #출력
    print(front - back)