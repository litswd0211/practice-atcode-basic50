import io,sys
with open("hand_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)

S=input()
S0=S[0]
S2=S[2]
ans = int(S0) * int(S2)
print(ans)