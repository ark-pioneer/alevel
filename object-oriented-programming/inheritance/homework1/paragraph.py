class Paragraph():
    def __init__(self, data):
        self.data = data

    def to_html(self):
        return "<p>" + self.data + "</p>"
        