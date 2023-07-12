import io,sys
with open("hand_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)

A, B, C = map(int, input().split())

if C % 2 == 0:
    if abs(A) < abs(B):
        print("<")
    elif abs(A) > abs(B):
        print(">")
    else:
        print("=")
else:
    if A >= 0 and B >= 0:
        if abs(A) < abs(B):
            print("<")
        elif abs(A) > abs(B):
            print(">")
        else:
            print("=")
    elif A >= 0 and B < 0:
        print(">")
    elif A < 0 and B >= 0:
        print("<")
    else:
        if abs(A) < abs(B):
            print(">")
        elif abs(A) > abs(B):
            print("<")
        else:
            print("=")