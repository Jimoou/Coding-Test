import sys

N = int(input())
meetingTime = []
for _ in range(N):
    meetingTime.append(list(map(int, sys.stdin.readline().split())))
meetingTime.sort(key=lambda x : (x[1], x[0]))

end = 0
m_Count = 0

for time in meetingTime:
    if end <= time[0]:
        end = time[1]
        m_Count += 1
        
print (m_Count)