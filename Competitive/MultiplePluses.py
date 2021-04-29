#Completed

EMPTY_STRING = ""
Storage = []
Final = []

# Function to break a string into all possible combinations of
# non-overlapping substrings appended in Storage[]
def recur(s, i, out):
    if i == len(s):
        Storage.append(out.split(" "))

    # considering each substring
    for j in reversed(range(i, len(s))):
        sub_str = s[i:j + 1] + " "          # append the substring to the result

         #recur with an index of the next character to be processed and the resultant string
        recur(s, j + 1, out + sub_str)


if __name__ == '__main__':
    # input string
    starting_index = 0
    for _ in range(int(input())):
        x, y = input().split("=")
        recur(x, starting_index, EMPTY_STRING)

        for x in Storage:
            x.pop(-1)
            String = "+".join(x)                #incorporating the '+' symbol in between the nos.
            if eval(String) == int(y):          #will Evaluate the expression
                Final.append(String.count("+"))
                break

    for x in Final:
        print(x)


