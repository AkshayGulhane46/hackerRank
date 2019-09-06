def average(array):
    # your code goes here
    #  print(set(array))
    ele = 0
    for ele1 in set(array):
        ele = ele1 + ele
    #  print(ele)
    length = len(set(array))
    sum = ele / length
    return sum


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)