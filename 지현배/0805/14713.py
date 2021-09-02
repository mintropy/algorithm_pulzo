import sys
ipt = sys.stdin.readline
N = int(ipt())
words = []
for _ in range(N):
    words.append(ipt().rstrip().split())
mixed_word = ipt().rstrip().split()
# 결과 기본 값은 True
res = True
# 문장을 뒤에서부터 확인한다.
for _ in range(len(mixed_word)):
    target = mixed_word.pop()
    # 앵무새가 한말들의 가장 뒤를 확인하고 일치하면 pop
    for n in range(N):
        if words[n] and words[n][-1] == target:
            words[n].pop()
            break
    # 하나도 일치 안하면 결과에 False 넣고 반복문 종료
    else:
        res = False
        break
if res == False:
    print('Impossible')
else:
    print('Possible')
