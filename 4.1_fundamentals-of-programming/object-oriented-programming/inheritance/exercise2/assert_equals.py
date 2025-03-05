class AssertEquals():
    def __init__(self, value, expected):
        self.value = value 
        self.expected = expected
    
    def class_name(self):
        return type(self).__name__
    
    def check(self):
        if self.value == self.expected:
            print("passed: ", self.class_name())
        else:
            print("failed:", self.class_name())
            print("\texpected:", self.expected, "got:", self.value)