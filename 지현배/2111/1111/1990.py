a, b = map(int, input().split())

palin_prime = [5, 7]

def checkPrime(num):
    for i in range(3, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def makePalindrome(n, part):
    palin = (part % 10) * 10

    for i in range(1, n - 1):
        palin += part % 10 ** (i + 1) // 10 ** i
        palin *= 10

    return palin * (10 ** (n - 1)) + part

def searchPalindrome(n, part):
    if n > 4:
        return

    fullpart = makePalindrome(n, part)

    if checkPrime(fullpart):
        palin_prime.append(fullpart)

    for i in range(10):
        searchPalindrome(n + 1, part + i * 10 ** n)

for i in [1, 3, 7, 9]:
    searchPalindrome(1, i)

palin_prime.sort()

# print(*tuple(filter(lambda x: a <= x <= b, palin_prime)), sep="\n")
for p in palin_prime:
    if a <= p <= b:
        print(p)
print(-1)