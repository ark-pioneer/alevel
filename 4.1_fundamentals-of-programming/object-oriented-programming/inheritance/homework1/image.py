from element import Element

class Image(Element):
    def to_html(self):
        return "<img src='" + self.data + "'/>"