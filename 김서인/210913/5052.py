# Trie !!
# https://youseop.github.io/2020-11-09-BAEKJOON-14425_%EB%AC%B8%EC%9E%90%EC%97%B4%EC%A7%91%ED%95%A9/
# 을 참고해서 Node, Trie 클래스를 구현했다.


class Node(object):

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head
        # string 문자 하나 하나 - 자식 노드 만들며 내려가기
        for char in string:
            # 자식 노드 중 같은 문자 없으면, 새로 생성
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            # 자식 노드 중 같은 문자 있으면, 거기로 이동
            current_node = current_node.children[char]

        current_node.data = string  # 마지막까지 오면(string의 끝이면) data에 string넣기

    def search(self, string):
        # string 완성되기 전에, 다른 게 완성되는지!- True, False로 리턴
        current_node = self.head
        for i in range(len(string) - 1):
            char = string[i]
            if char in current_node.children:
                current_node = current_node.children[char]

            if current_node.data:  # string 찾는 중간에 data 있는 current_node가 나오면(다른 번호가 이 번호의 접두어라는 뜻)
                return False

        return True


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    phone_numbers = list(input().strip() for _ in range(n))

    word_trie = Trie()
    # 넣기
    for i in range(n):
        word = phone_numbers[i]
        word_trie.insert(word)

    # 검사
    for i in range(n):
        word = phone_numbers[i]
        res = word_trie.search(word)
        if res == False:
            print('NO')
            break
    else:
        print('YES')
