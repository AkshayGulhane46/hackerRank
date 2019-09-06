# Task
# Read two integers a and b print two lines. The first line should contain integer division, a/b. // . The second line should contain float division,  / .
# #
# # You don't need to perform any rounding or formatting operations.
# #
# # Input Format
# #
# The first line contains the first integer, . The second line contains the second integer, .
#
# Output Format
#
# Print the two lines as described above.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c=(a/b)
    print(int(c))
    print('%.11f'%(c))
