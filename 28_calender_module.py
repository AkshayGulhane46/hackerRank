# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

# mm, dd, yyyy = input().split()

mm, dd, yyyy = map(int,input().split())


day=calendar.weekday(yyyy, mm, dd)

if(day==0):
 print("MONDAY")

if(day==1):
   print("TUESDAY")

if(day==2):
    print("WEDNESDAY")


if(day==3):
    print("THURSDAY")


if(day==4):
    print("FRIDAY")


if(day==5):
    print("SATURDAY")


if(day==6):
    print("SUNDAY")

