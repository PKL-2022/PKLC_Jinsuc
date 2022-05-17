# 2798
# 블랙잭
import sys

#모든 경우의수를 리스트에 담고 max로 정답 출력
# N = list(map(int, sys.stdin.readline().split()))
N = [10,500]
M = [93, 181 ,245 ,214 ,315 ,36 ,185 ,138 ,216 ,295]

i =0
j =1
k =2

# 리스트 초기화
result_list = []
# 경우의수 계산 
for a in range(len(M)*(len(M)-1)*(len(M)-2)):
    # 최대 값 이하 일때만 리스트에 담기
    if (M[i]+M[j]+M[k]) <= N[1]:
        result_list.append(M[i]+M[j]+M[k])
        # 순차적으로 검사 
        # 3자리 모두 마지막이면 종료
        if (M[i] ==M[-3])&(M[j]==M[-2])&(M[k]==M[-1]):
            break
        # 뒤에서 2자리 모두 마지막이면 1번째 자리수 다음으로
        elif (M[j] == M[-2])&(M[k]==M[-1]):
            i +=1
            j = i+1
            k = j+1
        # 뒤에서 1자리 마지막이면 두번째 자리수 다음으로
        elif (M[k] == M[-1]):
            j +=1
            k = j+1
        # 모든 자리수 마지막 아니면 3번째 자리 +1
        else:
            k+=1
    else:    
        if (M[i] ==M[-3])&(M[j]==M[-2])&(M[k]==M[-1]):
            break
        
        elif (M[j] == M[-2])&(M[k]==M[-1]):
            i +=1
            j = i+1
            k = j+1
        elif (M[k] == M[-1]):
            j +=1
            k = j+1
        else:
            k+=1
    
print(max(result_list))

print(N)