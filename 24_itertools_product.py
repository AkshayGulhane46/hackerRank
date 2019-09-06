# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

integer_list1 = list(map(int, input().split()))
integer_list2 = list(map(int, input().split()))

print(*product(integer_list1, integer_list2))
