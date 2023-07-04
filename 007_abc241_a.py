import io,sys
with open("hand_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)

a = list(map(int,input().split()))

i = 0
i = a[i]
i = a[i]
i = a[i]
print(i)
