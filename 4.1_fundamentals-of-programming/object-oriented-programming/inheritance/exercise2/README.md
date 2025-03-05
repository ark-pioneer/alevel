# Inheritance: Exercise 2
1. Refactor the current program code to take advantage of polymorphism.
2. Extract shared behaviour to a base class, overriding methods as needed, to take advantage of inheritance.
3. Extend the program with a third assertion type, taking advantage of your work so far. It should be fairly trivial now. Don't forget to instantiate the assertion and append it to the assertions list.

To implement: AssertIsEmpty
- for example `[]` should return `True`, but `[4, 59]` should return `False`

### Stretch
1. Find a way to show more information about each assertion
- each test should have a name that is printed in the output
- show the line number where the assertion failed
- show a summary of how many assertions were run, how many passed and how many failed