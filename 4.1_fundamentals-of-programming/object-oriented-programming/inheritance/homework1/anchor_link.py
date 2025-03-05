from element import Element

class AnchorLink(Element):
    def to_html(self):
        opening_tag = "<a " + self.name + "='" + self.value + "'" + ">"
        return opening_tag + self.data + "</a>"