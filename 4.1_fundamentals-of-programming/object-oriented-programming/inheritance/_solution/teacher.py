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

class TeacherAssistant()
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