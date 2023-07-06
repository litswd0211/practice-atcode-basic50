import io,sys
with open("hand_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)

N=int(input())
A=list(map(int,input().split()))
aSet = set(A)
print(len(aSet))