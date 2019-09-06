# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
#
# Input Format
# The first line contains a string consisting of space separated words.
#
# Output Format
# Print the formatted string as explained above.


def split_and_join(line):
    a = line.split(" ")  # a is converted to a list of strings.
    a = "-".join(a)
    return a

    # write your code here


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)