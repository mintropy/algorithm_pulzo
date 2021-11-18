import collections

arr = input()[6:-7]
# print(arr)
arr = arr.replace('<div ', '!')  # div 태그
arr = arr.replace('</div>', '')
arr = arr.replace('=', ' : ')  # = 가 들어가는 것은 div 태그의 title 에서 밖에 없으니까
arr = arr.replace('"', '')  # " 가 들어가는 것은 div 태그의 title에서밖에 없다.
arr = arr.replace('<p>', '@')  # p 태그
arr = arr.replace('</p>', '')

Q = collections.deque(arr)
res = []

while Q:
    temp = Q.popleft()

    # 다른 태그들 없애기
    if temp == '<':
        temp2 = Q.popleft()
        while temp2 != '>':
            temp2 = Q.popleft()
    else:
        res.append(temp)


res2 = ''.join(res)

res2 = res2.replace('>', '') # 다른 태그들 없애기 마무리 작업

res2 = ' '.join(res2.split()) # 공백이 연속적으로 있으면 하나만 남기기

res2 = res2.replace('@', '\n') # p 태그
res2 = res2.replace('!', '\n') # div 태그

res3 = list(res2.strip().split('\n')) # p 태그에서 시작, 끝 공백 없애려고

for tmp in res3:
    print(tmp)
