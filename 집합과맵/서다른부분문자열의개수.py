import sys

# 개행문자 제거 strip
S = sys.stdin.readline().strip()
s = []

start = 0
end = 0

while True:
    
    # S[0:0] ''가 리스트에 들어가는 것 방지
    if start == end:
        s.append(S[start])
        end +=1
        
    else:
        s.append(S[start:end+1])
        end +=1

    if end == len(S):
        start +=1
        end = start
        # start가 끝자리 오면 중지
        if start == len(S):
            break

# set으로 중복제거 다시 리스트로 변환 하여 길이 반환
s = list(set(s))
print(len(s))
