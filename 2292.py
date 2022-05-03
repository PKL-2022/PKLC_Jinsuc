#벌집

# 6배 등차 수열
import sys


n = int(sys.stdin.readline())

number = 1  
cnt = 1
while n > number :
    number += 6 * cnt  
    cnt += 1  
print(cnt)