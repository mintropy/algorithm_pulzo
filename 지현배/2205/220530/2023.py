import sys
input = sys.stdin.readline

N = int(input())

prime = {
    1: [2, 3, 5, 7]
}

def check(value):
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

for i in range(2, N + 1):
    prime[i] = []
    for p in prime[i - 1]:
        for j in range(5):
            if check(10 * p + 2 * j + 1):
                prime[i].append(10 * p + 2 * j + 1)

print(*prime[N], sep='\n')