# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby
nums = input()
for k, groups in groupby(nums):
    print((len(list(groups)),int(k)),end=" ")

