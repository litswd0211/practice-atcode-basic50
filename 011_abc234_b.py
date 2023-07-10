import io,sys
with open("hand_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)

import math

N = int(input())

x = []
y = []
for _ in range(N):
    x_, y_ = map(int, input().split())
    x.append(x_)
    y.append(y_)

ans = 0
for i in range(N):
    for j in range(i+1, N):
        length = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
        ans = max(ans, length)

print(ans)