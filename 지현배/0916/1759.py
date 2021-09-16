import sys
input = sys.stdin.readline
def sol():
    L, C = map(int, input().split())
    answer = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    # lastIndexOfvowel = -1
    words = input().split()
    words.sort()
    # for i in range(C):
    #     if words[i] in vowels:
    #         lastIndexOfvowel = i
    # if lastIndexOfvowel == -1:
    #     return answer
    def DFS(idx, cnt, password, vcnt):
        if cnt >= L:
            if vcnt > 0 and cnt - vcnt > 1:
                answer.append(password)
            return
        if idx >= C:
            return
        # if idx > lastIndexOfvowel and vcnt < 1:
        #     return
        if words[idx] in vowels:
            DFS(idx + 1, cnt + 1, password + words[idx], vcnt + 1)
        else:
            DFS(idx + 1, cnt + 1, password + words[idx], vcnt)
        DFS(idx + 1, cnt, password, vcnt)
    DFS(0, 0, '', 0)
    return answer
        

for e in sol():
    print(e)