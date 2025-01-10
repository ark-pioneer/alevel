from assert_equals import AssertEquals
from assert_less_than import AssertLessThan

assertions = [
    AssertEquals(4,5),
    AssertEquals("a","a"),
    AssertLessThan(6 , 10),
    AssertLessThan(9.2 , 3)
]

for assertion in assertions:
    assertion.check()