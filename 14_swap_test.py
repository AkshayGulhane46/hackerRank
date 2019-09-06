# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#
# For Example:
#
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
#

def swap_case(s):
    store = ""
    for alpha in s:
        curr = ord(alpha)
        if (curr >= 65 and curr <= 90):
            curr = curr + 32
            store = store + chr(curr)

        elif (curr >= 97 and curr <= 122):
            curr = curr - 32
            store = store + chr(curr)

        else:
            store = store + chr(curr)

    return store


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)