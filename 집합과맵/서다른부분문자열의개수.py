import sys

S = sys.stdin.readline()
s = []

# def recursive(S):
#     for i in range(len(S)):

for i in S:
    s.append(i)
    for a in range(len(S)-1):
        s.append(i+S[-a])
        for b in range(len(S)-2)

while len(S) 
