def sum_all(number_list):
    total = 0
    for num in number_list:
        num = int(num)
        total = num + total

    return int(total)

x = open("Grades.txt")
numberGrades = []
lineCount = 0
x.readline()
for line in x:
    ident, grade, letterGrade = line.split()
    numberGrades.append(int(grade))
    lineCount += 1
average = int(sum_all(numberGrades) / len(numberGrades))
print("Average grade is:", average)
print("Lowest grade was:", min(numberGrades))
print("Highest grade was:", max(numberGrades))
print("Final student count was:", lineCount)