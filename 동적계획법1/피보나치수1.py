# 24416번

import sys
n = int(sys.stdin.readline())

def fin(n):
    global cnt1
    if n ==1 or n == 2:
        return 1
    else:
        cnt1 += 1
        return (fin(n-1) + fin(n-2))

cnt1 = 0

# fin(1) fin(2)일 때도 계산해야 한다고 생각하지만 문제에서는 아니라고 함

'''
fin(5) = fin(4)+fin(3)

fin(4) = fin(3)+1
fin(3) = 1+1
'''

def fibonacci(n):
    global cnt2
    dp=[0 for i in range(n+1)]
    dp[1],dp[2]=1,1
    for i in range(3,n+1):
        cnt2 += 1
        dp[i]=dp[i-1]+dp[i-2]

    return cnt2

cnt2 = 0

fin(n)
fibonacci(n)

print(cnt1+1, cnt2)

# pypy3로 해야 시간초과 안생김