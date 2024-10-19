grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johhny','Bilbo','Steve','Khendrik','Aaron'}
sorted(students)
a = float(sum(grades[0])/len(grades[0]))
b =  float(sum(grades[1])/len(grades[1]))
c =  float(sum(grades[2])/len(grades[2]))
d =  float(sum(grades[3])/len(grades[3]))
f =  float(sum(grades[4])/len(grades[4]))
a1 = students[0]
b1 = students[1]
c1 = students[2]
d1 = students[3]
f1 = students[4]
school = { a1 : a, b1 : b, c1 : c, d1 : d, f1 : f}
print(school)