import sys

input = sys.stdin.readline
vowel = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()


def dfs(password, num, idx): # 그때까지 완성된 암호, 몇 자인지, arr[idx]를 보고 넣을지 말지
    if num == L:
        vowel_check = 0
        consonant_check = 0

        # 모음 1개 이상인지 확인
        for i in range(L):
            if password[i] in vowel: # 모음
                vowel_check += 1
            else: # 자음
                consonant_check += 1
        if vowel_check >= 1 and consonant_check >= 2: # 괜찮으면 출력
            print(password)
            return

    if idx >= C:
        return
    dfs(password + arr[idx], num + 1, idx + 1)
    dfs(password, num, idx + 1)


dfs('', 0, 0)

