# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
set1 = set(input().split())
m=input()
set2 = set(input().split())

union=set1.union(set2)
print(len(union))

