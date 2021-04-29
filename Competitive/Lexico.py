#Completed
T = int(input())
Lexicography = list("LEXICOGRAPHY")
Final = []

for _ in range(T):
    EmptyString = ""
    string = input()
    TestList = list(string.upper())

    for x in TestList:
        if x not in Lexicography:
            EmptyString = EmptyString + x
    Final.append(EmptyString)

for x in Final:
    print(x)