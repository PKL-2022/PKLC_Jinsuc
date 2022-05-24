#2108번

import sys
from collections import Counter

N = int(sys.stdin.readline())
num = []

for i in range(N):
    num.append(int(sys.stdin.readline()))

ssum = 0
for i in num:
    ssum += i
    
num.sort()

print(round(ssum/N)) #1
print(num[N//2])#2

#3
if len(num) ==1:
    print(num[0])
else:
    if Counter(num).most_common()[0][1] == Counter(num).most_common()[1][1]:
        print(Counter(num).most_common()[1][0])
    else:
        print(Counter(num).most_common()[0][0])
        
#4
print(len(range(min(num),max(num)+1))-1)