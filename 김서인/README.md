# 소감 & 배운 것 👩‍💻📝 (2021년 9월~ 11월)
12월부터는 각 달 폴더 안에 README를 쓰고 있습니다~ 

### 09.30.

[휴먼 파이프라인](https://www.acmicpc.net/problem/22981) 문제 : 잘 푼 것 같은데 계속 85% 에서 틀렸다. 결국 못 풀고 스터디에 참여했다. 태균님의 풀이를 들었는데, 내 코드와 거의 비슷했다. 마지막 부분에서 태균님이 작업 시간을 분 단위로 출력하기 위해서 %로 판단하셨다고 하면서, `math.ceil`을 써도 됐을 거라고 하셨다. 그러자 현배님, 효전님이 `ceil`을 써서 틀리다가 %로 푸셨다고 했다. `ceil`로 풀면 안 됐던 것이다. 나도 `ceil`부분만 고치니 맞았다. 다같이 왜 `ceil`은 안되는지 고민하다가 영준님이 부동 소수점 때문에 그런 것 같다고 하시며, 이런 문제는 %로 판단하는 게 나은 것 같다는 말씀을 하셨다. 앞으로도 문제를 풀다가 나누기를 할 때 이런 부분을 생각해야겠다 ! 

[외판원 순회 2](https://www.acmicpc.net/problem/10971) : DFS로 풀었다. 영준님이 N이 더 클 때도 사용할 수 있는 다른 방식을 설명해주셨는데, 더 공부해야겠다.

### 10.05.

이번에는 DP, 그리디 문제가 많았다. DP 식 세우는 것도 생각 안나고, 그리디 아이디어도 생각이 안나서 2문제만 풀었다ㅠㅠ 그리디.. DP...많이 푸는 것 밖에 답이 없겠지..??  

[여행](https://www.acmicpc.net/problem/2157)은 시간초과가 나왔다. DP로 시간을 줄여줘야지.

### 10.08.

이미 푼 문제(볼 모으기, 4연산)를 좀 더 간단하게 바꿀 수 있는 접근을 알게 되어서 재미있었다.

[샤워실 바닥 깔기(small)](https://www.acmicpc.net/problem/14600)는 알고리즘 분류가 분할 정복으로 되어 있는데, 어떻게 분할 정복으로 풀어야 할지 몰라서 못 풀었다. 다른 분들은 K가 1이거나 2니까 그 두 가지를 고려해서 푸셨다고 한다..! 알고리즘 분류에 연연하기 보다는, 문제와 조건을 잘 봐야겠다.

### 10.12.

나는 길게 늘려썼는데, 수학 공식을 활용하면 코드량도, 연산량도 줄어드는 [문제](https://www.acmicpc.net/problem/17392)가 있었다. 수학이 중요한 것 같다 ! 수학... 조금씩이라도 공부해야지.

[판치기](https://www.acmicpc.net/problem/23085) 문제는 어떻게 풀어야 할지,, 왜 BFS 인지 몰랐는데 설명(뒤집어진 동전의 개수를 방문 체크하는 것)을 듣고 이해가 되었다.

### 10.18.

최소 스패닝 트리를 구현할 때, 다익스트라로 할 수 있다는 것도 알게 되었다.

나는 [수열](https://www.acmicpc.net/problem/13274)문제, 태균님은 [최소 스패닝 트리](https://www.acmicpc.net/problem/1197)가 python  으로는 시간 초과가 나왔는데 pypy로 하니까 통과되었다.. ! python 시간 초과가 나왔을 때, pypy로도 정답인지 체크해보는 것도 좋을 것 같다.

[같은 수로 만들기](https://www.acmicpc.net/problem/2374).. 나는 못풀었는데, 현배&영준님이 분할 정복, 스택으로 푼 것을 알려주셨다. 두 가지 풀이가 있어서 재미있었다.



### 10.25.

백신 맞고 누워있어서, 문제를 하나밖에 못 풀었다...ㅠㅠ 그래도 다른 문제 고민이라도 해볼걸....  문제도 잘 안읽었더니, 다른 분들의 설명이 잘 이해되지 않는 것 같다.

꼭 문제를 풀지 못해도, 고민한 만큼 남으니까..!! 고민을 열심히 해야겠다.



### 10.28.

[BFS 스페셜 저지](https://www.acmicpc.net/problem/16940)문제는 50% 부근에서 틀렸는데 아무리 봐도 뭘 틀렸는지 몰랐다.ㅠㅠ 현배님과 영준님 설명을 들으면서 어떤 부분을 고쳐야 할지 알 수 있어서 좋았다. (1에서 출발하지 않는 경우, 깊이만 같은지 보면 안되고, 순서도 진짜 큐처럼 해야 한다는 것)

[RGB거리](https://www.acmicpc.net/problem/1149) 문제에서 dp 테이블을 작게 만들어도 되는 것을 알게 되었다! 직전 집을 각 색깔로 칠할 때 비용만 알면 돼서, 각 색깔 X 2로 만들어도 되는 것이었다. 



### 11. 01.

[구슬 게임](https://www.acmicpc.net/problem/2600)은 어떻게 풀지 몰랐는데, 풀이를 듣고 접근방법을 알 수 있었다.

[직사각형 색칠하기](https://www.acmicpc.net/problem/1186)는 문제 분류 중에 그리디가 있어서, 뭔가 엄청난(?) 방법을 떠올려야 할 것 같았다.. 하지만 생각이 전혀 나지 않아서 못 풀었다. 영준님이 많은 조건을 하나 하나 따져가면서 푸신 풀이를 보여주셨다! 많은 조건을 생각하고 구현하는 것도 연습이 필요할 것 같다.

[문자열 지옥에 빠진 호석](https://www.acmicpc.net/problem/20166)은 문제가 잘 이해가 되지 않았는데, 이해할 수 있었다. 영준님이 list로 in 검사를 해서 시간 초과 나오셨던 코드를 set으로 in 검사를 해서 통과하신 걸 보여주셨다. 



### 11.04.

이번 문제들은 주로 구현, 그리디, 게임이론 문제였다. DFS, BFS, 이분탐색 등등은 딱 어떻게 풀지 어느 정도 방법(??)이 있는데, 오늘 푼 문제들은 접근 방법을 생각하는 것부터 어려웠다. 

[고층 건물](https://www.acmicpc.net/problem/1027) 문제 - 나는 기울기를 활용해서 풀었는데, 사실 기울기 구하는 식도 확실히 모르겠어서 검색을 해봤다.. 중학교 수학... 화이팅..!!

[약수 지우기 게임1](https://www.acmicpc.net/problem/12107)- 어떻게 풀지 정말 감이 안잡혔는데, 풀이를 들으니 이해는 되었다. 이런 생각을 어떻게 하지??! 여러 문제를 많이 만나 봐야겠다.

[빗물](https://www.acmicpc.net/problem/14719) - 나는 좀 비효율적으로 풀었는데, 다른 분들이 좀 더 효율적으로 푸신 것을 봐서 재미있었다.

### 11. 08.
[20302 민트 초코](https://www.acmicpc.net/problem/20302).. 며칠 전부터 어떻게 푸는지 궁금했는데, 오늘 영준님의 설명을 듣고 나서 풀었다!! ㅎㅎ 10001까지의 소수를 모두 구하고, 각 정수가 어떻게 소인수 분해 되는지 돌아볼 때 10001까지 다 보면 시간 초과가 난다. 거기에 루트 씌운 것까지만 소수를 구하고, 거기까지만 봐도 된다. 그리고 나서 10001에 루트씌운 것까지의 소수로도 안 나눠지면, 10001에 루트 씌운 것보다 큰 소수라는 것이다.

[16884 나이트 게임](https://www.acmicpc.net/problem/16884) N이 1~4까지 그려보고 감으로(??) 풀었다. 정확히 설명, 증명하지는 못했는데 다른 분들의 설명을 들으니 더 분명해지는 것 같다.

[17144 미세먼지 안녕!](https://www.acmicpc.net/problem/17144) 어떤 부분에서 시간이 오래 걸렸는지 알 수 있었다! 나는 매초 격자판을 쭉 보면서 미세먼지의 인덱스와 양을 리스트에 저장했다. 그런데 영준&태균님은 굳이 그렇게 쭉 보지 않고,, 리스트를 복사해서 쓰는 방법으로 푸셨다.

### 11. 11.

[20008 몬스터를 처치하라](https://www.acmicpc.net/problem/20008) 문제..! 계속 시간초과가 나서 고민하고 있었는데, 영준님의 설명을 듣고 풀었다. 나는 1초씩 증가하면서 스킬을 사용할 수 있는지 보았는데, 영준님은 스킬 대기 시간만큼 증가하셨다. 

[4811 알약](https://www.acmicpc.net/problem/4811) 문제. 4초 정도까지는 경우를 생각해봤지만 못풀었는데, 설명에서 카탈란 수!!라는 걸 알았다.  나름 유명한 수열인 것 같다.

[1990 소수 인 팰린드롬](https://www.acmicpc.net/problem/1990)- 답을 구글링해보면 짝수는 안되고 홀수개만 된다.  이런 이야기가 있는데 잘 이해가 안됐는데, 설명을 듣고 알게 되었다. 11을 제외한 짝수 개는 11로 묶을 수 있다. (그러니까 소수가 아니다)



### 11.15

[돌 게임 6](https://www.acmicpc.net/problem/9660) - 얼마 전부터 스터디에서 게임 이론 문제를 풀고 있어서 좋다. 이 것도 게임이론 문제인데, 못 풀고 있었다. 효전님의 설명을 듣고 이해할 수 있었다. 범위를 보면서 어떤 식으로 풀지 생각하고, 규칙을 찾으려고 노력해보는 것을 배울 수 있었다.

[1897 토달기](https://www.acmicpc.net/problem/1897) 나는 python은 시간 초과, pypy로 힘겹게 통과했다. 영준님의 설명을 듣고, 어떻게 시간을 줄일 수 있을지 생각해볼 수 있었다.

[3107 IPv6](https://www.acmicpc.net/problem/3107)  zfill 이라는 함수를 알게 되었다. 문자열이나 숫자를 특정한 자릿수로 만들어주고 싶을 떄, 부족한 만큼 앞에 0을 채워준다.  문자열이나숫자.zfill(몇자리)



### 11.18

[공주님을 구해라](https://www.acmicpc.net/problem/17836) : 나는 검을 얻은 후에도 계속 bfs를 했는데, 다른 분들은 검을 얻은 후에는 그 위치에서 최소 거리로 목적지에 도착하는 걸 계산한 후에 끝내셨다. 나는 일단은 통과했지만 사이즈가 더 커지고, 검이 앞쪽에서 나오고.. 하면 q 안에 들어가는 게 더 많아서 시간이 오래 걸릴 것이다. 나는 저런 아이디어를 생각 못했는데, 저런 풀이를 보면서 배울 수 있었다.

[경로 게임](https://www.acmicpc.net/problem/12887), [앱](https://www.acmicpc.net/problem/7579), [AB](https://www.acmicpc.net/problem/12970)   나는 셋 다 못 풀었다..ㅠ 다른 분들이 설명해주셨는데, 여러 경우를 생각해 보신 후에 규칙을 깨달아서 풀었다고 하셨다. 나도 더 깊이, 오래 생각해보고 여러 경우를 그려봐야겠다..!!



