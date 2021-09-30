import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
st = []
def hanoi(n, fr, via, to):
    if n == 0:
        return
    hanoi(n-1, fr, to, via)
    #print(fr, to)
    st.append((fr, to))
    hanoi(n-1, via, fr, to)

hanoi(N,1,2,3)
print(len(st))
for v in st:
    print(*v)