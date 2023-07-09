import io,sys
with open("hand_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)

N=int(input())
Mountains = []
for i in range(N):
    S, T = map(str, input().split())
    T = int(T)
    Mountains.append([T, S])

Mountains.sort(reverse=True)

print(Mountains[1][1])
