 # Enter your code here. Read input from STDIN. Print output to STDOUT

for test in range(int(input())):
    try:
        x,y=map(int,input().split())
        div_res=x//y
        print(div_res)
    except ZeroDivisionError as e:
           print("Error Code:",e)
    except ValueError  as e:
           print("Error Code:",e)


# for test in range(int(input())):
#     try:
#         a,b = map(int,input().split())
#         division_result = a // b
#         print(division_result)
#     except ZeroDivisionError as e:
#         print("Error Code:",e)
#     except ValueError as e:
#         print("Error Code:",e)
