c1, c2, c3, c4, c5, c6 = map(int, input().split())
# 최대공약수
def gcd(p, q):
    if q == 0: return p
    return gcd(q, p % q)
# c1과 c5의 최대공약수는 x2
x2 = gcd(c1, c5)
x1 = c1 // x2
x3 = c5 // x2
# c3와 c6의 최대공약수는 x6
x6 = gcd(c3, c6)
x5 = c6 // x6
x7 = c3 // x6
print(x1, x2, x3, x5, x6, x7)