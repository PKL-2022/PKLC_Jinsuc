# 14425

import sys

N, M = map(int, sys.stdin.readline().split())

S = []
result = 0

for n in range(N):
    S.append(sys.stdin.readline())

# 검사를 통해서 S집합 안에 있으면 +1을 해줌
for m in range(M):
    if sys.stdin.readline() in S:
        result +=1

print(result)