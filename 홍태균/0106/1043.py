'''
거짓말

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

true = list(map(int,input().split()))

# 진실을 말해야하는 친구
true_people = []
if true[0]:
    true_people += true[1:]
# 파티들 저장
parties = []

for _ in range(M):
    in_party = list(map(int,input().split()))
    for person in in_party[1:]:
        # 파티에 진실을 말해야하는 친구 여부
        # 있다면 해당 파티의 친구들을 다 진실을 말해야하는 리스트에 저장
        # 그 후 set으로 중복 제거
        if person in true_people:
            true_people += in_party[1:]
            true_people = list(set(true_people))
            break
    # 만약 파티에 진실을 말해야하는 친구가 없다면 파티를 저장
    else:
        parties.append(in_party[1:])

# while을 빠져나오기 위해
# 더 이상 진실을 말할 친구가 없을 때
plag = True

while plag:
    plag = False
    # 이전 새 파티들을 저장하기 위해서
    preparty = []
    # 각 파티의 친구들을 진실 여부를 판단
    for party in parties:
        for person in party:
            # 진실을 말해야한다면
            if person in true_people:
                # 변경사항이 생겼기 때문에 다시 while을 돌기 위해서
                plag = True
                # 위와 같이 해당 파티의 친구들을 진실을 말해야하는 친구에 저장
                true_people += party
                true_people = list(set(true_people))
                break
        # 만약 그러한 친구가 없다면 새 파티리스트에 저장
        else:
            preparty.append(party)
    # 새파티 저장
    parties = preparty

# 남아있는 파티 갯수가 진실을 안 말해도 되는 파티
print(len(parties))
