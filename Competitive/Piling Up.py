# COMPLETE
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

for _ in range(int(input())):
    n = int(input())
    LI = []
    t = deque(int(i) for i in input().split())

    while len(LI) != n:
        if t[0] >= t[-1]:
            LI.append(int(t.popleft()))
        else:
            LI.append(int(t.pop()))
    TI = LI.copy()
    LI.sort(reverse=True)
    if TI == LI:
        print("Yes")
    else:
        print("No")