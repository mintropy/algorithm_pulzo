import collections
import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

d, first_word = input().split()
words = list(input().strip() for _ in range(int(d)))
ans = 0


# target_word에서 한 글자 토 달기해서 사전에 있는 단어 만들 수 있는지
def check(target_word):
    after_words = []
    target_word_len = len(target_word)
    for word in words:  # 사전의 단어
        # 글자 수 하나만 더 많아야 함
        if (target_word_len + 1) != len(word):
            continue

        # 포함 되면(맨 앞이나 맨 뒤에 붙는 것)
        if target_word in word:
            after_words.append(word)
            continue

        # 중간에 포함되는지
        target_word_idx = 0
        word_idx = 0
        while word_idx < len(word):
            if word[word_idx] == target_word[target_word_idx]:
                target_word_idx += 1
            word_idx += 1
        if target_word_idx == len(target_word):
            after_words.append(word)

    return after_words


# 사전에 있고, 토 달기한 단어를 BFS에 넣어 주기
def bfs():
    global ans

    q = collections.deque()
    q.append(first_word)

    while q:
        word = q.popleft()

        ans = word

        tmp = check(word)
        q.extend(tmp)

    return

bfs()
print(ans)
