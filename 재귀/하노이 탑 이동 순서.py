#하노이 탑 이동 순서 11729번
#아직 이해가 잘 안되서 가져와서 이해하려 했습니다..

import sys

# num: 옮겨야하는 수 / f: from / b: 거쳐서 / t: to
def hanoi(num, f, b, t):
    if num == 1:
        print(f, t)
    else:
        hanoi(num-1, f, t, b)
        print(f, t)
        hanoi(num-1, b, f, t)

num = int(sys.stdin.readline())
print(2**num - 1)
hanoi(num, 1, 2, 3)