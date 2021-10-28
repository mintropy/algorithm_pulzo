N = int(input())
minn = 100
maxx = 0
def sol(num, summ):
    if num < 10:
        global maxx, minn
        if num % 2: summ += 1
        if maxx < summ: maxx = summ
        if minn > summ: minn = summ
    elif num < 100:
        if num % 2: summ += 1
        if num // 10 % 2: summ += 1
        sol(num % 10 + num // 10, summ)
    else:
        n = num
        while n:
            if n % 2: summ += 1
            n //= 10
        s = str(num)
        length = len(s)
        for i in range(1, length - 1):
            for j in range(i + 1, length):
                front = int(s[0:i])
                middle = int(s[i:j])
                back = int(s[j:])
                sol(front + middle + back, summ)
sol(N, 0)
print(minn, maxx)