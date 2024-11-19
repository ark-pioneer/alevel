class AssertLessThan():
    def __init__(self, value, expected):
        self.value = value
        self.expected = expected

    def class_name(self):
        return type(self).__name__
    
    def check_less_than(self):
        if self.value < self.expected:
            print("passed: ", self.class_name())
        else:
            print("failed: ", self.class_name())
            print("\texpected: True", "got: False")
            
class AssertEquals():
    def __init__(self, value, expected):
        self.value = value 
        self.expected = expected
    
    def class_name(self):
        return type(self).__name__
    
    def check_equals(self):
        if self.value == self.expected:
            print("passed: ", self.class_name())
        else:
            print("failed:", self.class_name())
            print("\texpected:", self.expected, "got:", self.value)

assertions = [
    AssertEquals(4,5),
    AssertEquals("a","a"),
    AssertLessThan(6 , 10),
    AssertLessThan(9.2 , 3)
]

for assertion in assertions:
    if type(assertion) is AssertEquals:
        assertion.check_equals()
    elif type(assertion) is AssertLessThan:
        assertion.check_less_than()