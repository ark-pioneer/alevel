from element import Element

class Heading1(Element):
    def to_html(self):
        return "<h1>" + self.data + "</h1>"
