# Enter your code here. Read input from STDIN. Print output to STDOUT

# s = set('HackerRank')
# s.add('H')
# print s
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# print s.add('HackerRank')
# None
# print s
# set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])
s = set('')
n = input()
n = int(n)
for i in range(n):
    s.add(input())

print(len(s))
