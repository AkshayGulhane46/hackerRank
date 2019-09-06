# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
array,num = input().split()
sorted(array)

per=permutations(array,int(num))
for i in per:
 print(''.join(i),sep='\n')


