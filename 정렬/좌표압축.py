# 18870번

# 핵심은 중복을 제거한 정렬

import sys
N = int(sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))

# X_ = []
# for i in X:
#     if i not in X_:
#         X_.append(i)
# 위 함수 쓰니 시간초과
X_ = list(set(X))

X_.sort()



X_dict = dict()
for idx,i in enumerate(X_):
    X_dict[i] = idx

for _ in X:
    print(X_dict[_], end = ' ')