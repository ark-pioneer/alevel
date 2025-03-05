from element import Element

class Paragraph(Element):
    def to_html(self):
        opening_tag = "<p " + self.name + "='" + self.value + "'" + ">"
        return opening_tag + self.data + "</p>"
        