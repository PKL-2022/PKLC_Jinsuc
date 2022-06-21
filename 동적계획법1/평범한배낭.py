# 12865

import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    table = [0]*(k+1)
    for _ in range(n):
        w, v = map(int, sys.stdin.readline().split())
        if w > k:
            continue
        # 최대 w값부터 내려오게 됨
        for j in range(k, 0, -1):
            if j + w <= k and table[j] != 0:
                table[j+w] = max(table[j+w], table[j] + v)
        table[w] = max(table[w], v)
    print(max(table))

solve()

'''
W A B C D
0 0 0 0 0
1 0 0 0 0
2 0 0 0 0
3 0 0 6 6
4 0 8 8 8
5 0 0 0 12
6 13 13 13 13  
7 0 0 14 14 
'''