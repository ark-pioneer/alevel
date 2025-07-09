class Person():
    def __init__(self, fname, lname, age):
        self.__fname = fname
        self.__lname = lname
        self.__age = age

    def summary(self):
        return f"{self.__fullname()} is {self.__age}"

    def __fullname(self):
        return f"{self.__fname} {self.__lname}"

p = Person("Henry", "Misewe", 17)
# print(p.__fullname())
# print(p.__age)

print(p.summary())