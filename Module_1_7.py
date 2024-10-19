grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johhny','Bilbo','Steve','Khendrik','Aaron'}
list_ = sorted(students)
a = float(sum(grades[0])/len(grades[0]))
b =  float(sum(grades[1])/len(grades[1]))
c =  float(sum(grades[2])/len(grades[2]))
d =  float(sum(grades[3])/len(grades[3]))
f =  float(sum(grades[4])/len(grades[4]))
a1 = list_[0]
b1 = list_[1]
c1 = list_[2]
d1 = list_[3]
f1 = list_[4]
school = { a1 : a, b1 : b, c1 : c, d1 : d, f1 : f}
print(school)