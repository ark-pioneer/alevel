class Animal():
    def __init__(self, name):
        self._name = name

    def greet(self):
        return self.__greeting() + self._name

    def __greeting(self):
        return "Hello, my name is "

a = Animal("leopard")
print(a.greet())
print(a._name)
print(a.__greeting())

