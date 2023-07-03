import io,sys
with open("hand_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)

P=list(map(int,input().split()))
ans=""

for i in range(26):
    ans+=chr(P[i]+96)

print(ans)