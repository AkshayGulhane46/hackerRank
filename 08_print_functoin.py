# Read an integer N.
#
# Without using any string methods, try to print the following:
#
# 123.....N
#
#
# Note that "" represents the values in between.
#
# Input Format
#
# The first line contains an integer N.

if __name__ == '__main__':
    n = int(input())
    count = 1
    while (count != n + 1):
        print(count, end="")
        count = count + 1

