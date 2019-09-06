# You have a record of N students. Each
# record contains the student's name, and their percent marks in Maths,' \
#                            ' Physics and Chemistry. The marks can be floating' \
#                            ' values. The user '
#                            'enters some integer ' \
#                            ' N followed by the names and marks for  students. You are' \
#                            ' required to save the record in a dictionary data type. ' \
#                            'The user then enters a student's name. Output the average
# percentage marks obtained by that student, correct to two decimal places.
#
# Input Format
#
# The first line contains the integer , the number of students. The next
# lines contains the name and marks obtained by that student separated by a space.
# The final line contains the name of a particular student previously listed.

if __name__ == '__main__':
    n = int(input())
    add = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

# print(query_name)

newlist = student_marks[query_name]
# print(newlist)
for ele in newlist:
    add = add + ele

add = add / 3
print("%.2f" % add)
