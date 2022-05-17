# 1436번
import sys

N = int(sys.stdin.readline())

# 모든 경우의수 출력

end = 666 #666 초기화
while True:
    if '666' in str(end): #666이들어가 있으 때만 N-1
        N = N-1
        if N == 0: # N이 0되면 종료
            break
    end = end + 1

print(end)