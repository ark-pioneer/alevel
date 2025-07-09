class Teacher():
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def teach(self):
        return "lots of teaching delivered"
    def allocation(self):
        return 23

class HeadOfDepartment():
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def teach(self):
        return "lots of teaching delivered"     
    def allocation(self):
        return 21

class TeacherAssistant():
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def teach(self):
        return "lots of teaching delivered"
    def allocation(self):
        return 24

# Instructions
# 1. identify the shared behaviour
# 2. encapsulate the shared behaviour in a base class
# 3. Inherit from the base class in the appropriate child classes. 

t = Teacher("Miss B. Aviour", "Business")
hod = HeadOfDepartment("Mr. Withers", "Computer Science")
ta = TeacherAssistant("Mr. Smith", "Computer Science")

print("teacher")
print(t.teach())
print(t.allocation())

print("head of department")
print(hod.teach())
print(hod.allocation())

print("teacher assistant")
print(ta.teach())
print(ta.allocation())

# extension:
# 1. Add another staff member following the pattern.
# Inherit from two parent classes!