# Given the participants' score sheet for your University Sports Day, you are ' \
#                       'required to find the runner-up score.' \
#                       ' You are given n scores. Store them in a list and ' \
#                       'find the score of the runner-up.

def largest(arr):
    final_list = []
    for num in arr:
        if num not in final_list:
            final_list.append(num)
        #   print(final_list[:])
    final_list.sort(reverse=True)
    print(final_list[1])


if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()))
    largest(arr)
