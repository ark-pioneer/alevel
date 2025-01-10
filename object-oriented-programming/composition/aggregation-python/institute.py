class Institute():
    def __init__(self, instituteName, deparments):
        self.instituteName = instituteName
        self.departments = deparments
    
    def getTotalStudentsInInstitute(self):
        noOfStudents = 0
        for dept in self.departments:
            noOfStudents += len(dept.getStudents())

        return noOfStudents
