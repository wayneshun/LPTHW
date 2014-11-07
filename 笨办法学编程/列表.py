students = [['Zhang',60],['Wang',90],['Li',81],['Xu',100]]

print float(sum([student[1] for student in students])) / len(students)

print [n*n for n in range(7) if n*n % 2 == 0]

L = [1, 2, 3, 4]

print ''.join([str(i) for i in L])