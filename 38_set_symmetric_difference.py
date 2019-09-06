# Enter your code here. Read input from STDIN. Print output to STDOUT
a=input()
set1=set(input().split())
b=input()
set2=set(input().split())
c=set1.symmetric_difference(set2)
print(len(c))
