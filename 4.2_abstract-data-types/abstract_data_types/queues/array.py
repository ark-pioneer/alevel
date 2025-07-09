class Array():
    def __init__(self, items):
        if len(set([type(item) for item in items])) > 1:
            raise TypeError
        self.__items = items

    def __str__(self):
        return str(self.__items)

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, arg):
        return self.__items[arg]

    def __setitem__(self, arg, value):
        self.__items[arg] = value
