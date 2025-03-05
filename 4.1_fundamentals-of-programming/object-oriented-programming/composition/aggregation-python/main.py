from student import Student
from department import Department
from institute import Institute

s1 = Student("Mia", 1, "CSE")
s2 = Student("Priya", 2, "CSE")
s3 = Student("John", 1, "EE")
s4 = Student("Rahul", 2, "EE")

cse_students = []
cse_students.append(s1)
cse_students.append(s2)

ee_students = []
ee_students.append(s3)
ee_students.append(s4)

CSE = Department("CSE", cse_students)
EE = Department("EE", ee_students)

departments = []
departments.append(CSE)
departments.append(EE)

institute = Institute("BITS", departments)

print("Total students in institute: " + str(institute.getTotalStudentsInInstitute()))