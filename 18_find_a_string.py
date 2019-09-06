def count_substring(string, sub_string):
    length_string = len(string)
    length_substring = len(sub_string)

    return (sum([1 for i in range(0, length_string - length_substring + 1)
                 if (string[i:(length_substring + i)] == sub_string)]))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)