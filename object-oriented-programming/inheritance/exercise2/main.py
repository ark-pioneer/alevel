from assert_equals import AssertEquals
from assert_less_than import AssertLessThan

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