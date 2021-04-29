#completed
Final = []
combi = []

for _ in range(int(input())):
    counter = 0
    s_one = input()
    s_two = input()

    if s_one == s_two:
        Final.append(counter)

    else:
        small = min(s_one,s_two,key=len)
        large = max(s_one,s_two,key=len)
        ns = len(small)
        nl = len(large)

        for i in range(ns):
            for j in reversed(range(i,ns)):
                temp = small[i:j+1]
                if temp not in combi:
                    combi.append(temp)

        combi.sort(key=len,reverse=True)

        for x in combi:
            if x in large:
                counter = (ns - len(x)) + (nl - len(x))
                break
        if counter == 0:
            counter = nl + ns

        Final.append(counter)

for x in Final:
    print(x)