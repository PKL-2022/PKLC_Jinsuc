#분수찾기

# 1/1 → 1/2 → 2/1 → 3/1 → 2/2 1/3 1/4 2/3 3/2 2/4
# 대각선으로 지그재그 움직임

# 짝수 1/2 2/1 분모부터 
# 홀수 3/1 2/2 1/3 분자부터

import sys 

N=int(sys.stdin.readline())

number=1
while N>number:
    N-=number
    number+=1
    
if number%2==0:
    a=N
    b=number-N+1
else:
    a=number-N+1
    b=N
    
print(f'{a}/{b}')


