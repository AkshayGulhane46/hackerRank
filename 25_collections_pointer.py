# Enter your code here. Read input from STDIN. Print output to STDOUT

# x=input()
# ss=input().split()
# n=input()
# s=[]
# i=0
# for i in range(int(n)):
#  input().split()


# print(x)
# print(ss)
# print(n)
# print(i)

import collections

numShoes = int(input())
shoes = collections.Counter(map(int,input().split()))
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int,input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print(income)
