class Heading1():
    def __init__(self, data):
        self.data = data

    def to_html(self):
        return "<h1>" + self.data + "</h1>"
