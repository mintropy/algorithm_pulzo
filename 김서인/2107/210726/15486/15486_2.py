def DFS(depth,money):
    global sum
    if depth>n:
        return
    if depth==n:
        if money>sum:
            sum=money
    else:
        DFS(depth+get_money[depth],money+need_time[depth])
        DFS(depth+1,money)

if __name__ == "__main__":
    n=int(input())
    need_time=list()
    get_money=list()

    for _ in range(n):
        a,b=map(int,input().split())
        get_money.append(a)
        need_time.append(b)
        

    sum=0

    DFS(0,0)
    print(sum)