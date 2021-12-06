N = int(input())
def sol(n):
    if n == 0:
        return 1
    
    num = sol(n // 2)
    if n % 2:
        return 2 * num * num % (10 ** 9 + 7)
    else:
        return num * num % (10 ** 9 + 7)
print(sol(N - 1) if N != 0 else 1)