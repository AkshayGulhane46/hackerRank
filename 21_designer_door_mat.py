# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n,m = map(int,sys.stdin.readline().split())

mid =int(n/2)
mid2=int(m/2)

for i in range(0,mid2):
        if(i%2!=0):
            if (i == n):
                break
            else:
             print("---"*mid+".|."*(i) + "---"*mid)
             mid=mid-1


print("WELCOME".center(m,"-"))

n=n-2
j=1
for i in range(n,0,-1):
    if(i%2!=0):
     print("---"*j +".|."*n+"---"*j)
     n=n-2
     j=j+1
