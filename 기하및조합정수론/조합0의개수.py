# 2004번

import sys

n,m = map(int, sys.stdin.readline().split())

if n == m or m ==0:
    print(0)
else:
    n_list = [n-i if i >0 else n for i in range(0, m)]
    m_list = [i for i in range(1, m+1)]

    parent = 1
    child = 1

    for p in n_list:
        child *= p
    for c in m_list:
        parent *= c
    cnt = 0
    a = [i for i in str(child//parent)]
    for i in a[::-1]:
        if i =='0':
            cnt += 1
        else:
            break
    print(cnt)
        
# 정답 코드 소인수 분해로 풀라함 ;;

n,m=map(int,input().split())

def factorial_5or2_cnt(num,t):
  cnt=0
  while num>0:
    cnt+=num//t
    num//=t
  return cnt

cnt_5=factorial_5or2_cnt(n,5)-factorial_5or2_cnt(m,5)-factorial_5or2_cnt(n-m,5)
cnt_2=factorial_5or2_cnt(n,2)-factorial_5or2_cnt(m,2)-factorial_5or2_cnt(n-m,2)
result=min(cnt_5,cnt_2)
print(result)        