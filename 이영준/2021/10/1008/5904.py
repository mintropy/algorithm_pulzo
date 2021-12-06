"""
Title : Moo 게임
Link : https://www.acmicpc.net/problem/5904
"""

n = int(input())

Moo_words = []

a, b = 3, 4
while a <= n:
    Moo_words.append(a)
    a += a + b
    b += 1
b -= 1

ans = ''
# 단어를 하나씩 빼면서 확인
while Moo_words and not ans:
    length = Moo_words.pop()
    if n <= length:
        b -= 1
    elif length < n <= length + b:
        if n == length + 1:
            ans = 'm'
        else:
            ans = 'o'
        break
    else:
        n -= (length + b)
        b -= 1

if ans:
    print(ans)
elif n == 1:
    print('m')
elif n <= 3:
    print('o')


'''
Counter Example
10
ans : o
'''
