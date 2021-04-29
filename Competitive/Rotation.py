T = int(input())
samp = [""]
samp2 = [""]
Final = [""]

for x in range(T):
    samp[x] = input()
    samp2[x] = input()

    Listsamp = samp[x].split()
    N, K = int(Listsamp[0]), int(Listsamp[-1])

    A = samp2[x].split()
    Aout = A.copy()

    i = -K
    for x in range(N):
        Aout[x] = (A[i])
        i = i + 1

    temp = " ".join(Aout)
    Final.append(temp)

Final.pop(0)
for x in range(T):
    print(Final[x])
