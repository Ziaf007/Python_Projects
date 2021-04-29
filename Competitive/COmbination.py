EMPTY_STRING = ""
Storage = []

# Function to break a string into all possible combinations of
# non-overlapping substrings enclosed within parenthesis
def recur(s, i, out):
    if i == len(s):
        Storage.append(out.split(" "))

    # consider each substring `S[i, j]`
    for j in reversed(range(i, len(s))):
        sub_str = s[i:j + 1] + " "

        # append the substring to the result and recur with an index of the
        # next character to be processed and the result string
        recur(s, j + 1, out + sub_str)


if __name__ == '__main__':
    # input string
    s = "4481"

    starting_index = 0
    recur(s, starting_index, EMPTY_STRING)

    print(Storage)